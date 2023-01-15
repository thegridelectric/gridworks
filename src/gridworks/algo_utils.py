import base64
import logging
from functools import cached_property
from hashlib import shake_256
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from typing import no_type_check

import dotenv
from algosdk import account  # type: ignore[import]
from algosdk import encoding
from algosdk import mnemonic
from algosdk.atomic_transaction_composer import AccountTransactionSigner
from algosdk.future import transaction  # type: ignore[import]
from algosdk.future.transaction import Multisig  # type: ignore[import]
from algosdk.future.transaction import MultisigTransaction
from algosdk.kmd import KMDClient  # type: ignore[import]
from algosdk.v2client.algod import AlgodClient  # type: ignore[import]
from pyteal import Expr
from pyteal import Mode
from pyteal import compileTeal

import gridworks.errors as errors
import gridworks.property_format as property_format
from gridworks import gw_config


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


def address_to_public_key(addr: str) -> str:
    return str(base64.b32encode(encoding.decode_address(addr)).decode())


def public_key_to_address(pubKey: str) -> str:
    return str(encoding.encode_address(base64.b32decode(pubKey)))


def string_2_32byte_hash(input_str: str) -> bytes:
    return shake_256(input_str.encode("utf-8")).digest(32)


def string_to_algo_addr(input_str: str) -> str:
    """Encodes a string as an algorand address. Could be used to
    overload mutable optional address fields in an asset (freeze,
    reserve, clawback)

    Args:
        input_str: Aribtrary string.

    Returns:
        str: AlgoAddressStringFormat
    """
    fakeHash1 = string_2_32byte_hash(input_str)
    fakeHash1_as_address = encoding.encode_address(fakeHash1)
    assert encoding.is_valid_address(fakeHash1_as_address)
    return str(fakeHash1_as_address)


##############################################################################
# App related helpers
##############################################################################


def decode_state(state_array: List[Any]) -> Dict[bytes, Union[int, bytes]]:
    state: Dict[bytes, Union[int, bytes]] = dict()

    for pair in state_array:
        key = base64.b64decode(pair["key"])

        value = pair["value"]
        valueType = value["type"]

        if valueType == 2:
            # value is uint64
            value = value.get("uint", 0)
        elif valueType == 1:
            # value is byte array
            value = base64.b64decode(value.get("bytes", ""))
        else:
            raise Exception(f"Unexpected state type: {valueType}")

        state[key] = value

    return state


def get_app_global_state(
    client: AlgodClient, app_id: int
) -> Dict[bytes, Union[int, bytes]]:
    """Returns the global state of an Algorand application

    Args:
        client: Any AlgodClient
        app_id (int): the application id of the smart contract

    Returns:
        Dict[bytes, Union[int, bytes]]: Returns the decoded key/value
        pairs of an app's global state (uints and bytes)
    """
    appInfo = client.application_info(app_id)
    return decode_state(appInfo["params"]["global-state"])


def fully_compile_contract(client: AlgodClient, contract: Expr) -> bytes:
    teal = compileTeal(contract, mode=Mode.Application, version=5)
    response = client.compile(teal)
    return base64.b64decode(response["result"])


##############################################################################
# Getting Algod and KMD clients using the config file for settings and secrets
##############################################################################


def get_kmd_client(settings: gw_config.VanillaSettings) -> KMDClient:
    return KMDClient(
        settings.algo_api_secrets.kmd_token.get_secret_value(),
        settings.public.kmd_address,
    )


#####################################
# Wrapper classes for stronger typing
#####################################


class BasicAccount:
    """Representation of the public and private information of an Algorand
    account, with a few shorthands on top of algosdk.account - in particular
    x = BasicAccount() will generate a new BasicAccount.
    """

    def __init__(
        self,
        private_key: Optional[str] = None,
    ) -> None:
        if private_key is None:
            private_key = account.generate_account()[0]
        self._sk: str = private_key
        self._addr: str = account.address_from_private_key(private_key)

    def as_signer(self) -> AccountTransactionSigner:
        return AccountTransactionSigner(self.sk)

    @cached_property
    def sk(self) -> str:
        """Shorthand for the account's private key"""
        return self._sk

    @cached_property
    def addr(self) -> str:
        """Shorthand property for the account's public key"""
        return self._addr

    def address(self) -> str:
        """A method returning the account's public key. Equivalent to self.addr"""
        return self._addr

    def private_key(self) -> str:
        """A method returning the account's private key. Equivalent to self.sk"""
        return self._sk

    @cached_property
    def address_as_bytes(self) -> bytes:
        """Useful if digging into encoding and decoding between strings and bytes."""
        return bytes(encoding.decode_address(self.addr))

    @cached_property
    def mnemonic(self) -> str:
        """m stands for `mnemonic`, the string of 25 words
        that has equivalent information content to the private key
        """
        return str(mnemonic.from_private_key(self._sk))

    @cached_property
    def addr_short_hand(self) -> str:
        """Returns the last 6 characters of the account address.
        Used for logging messages and human eyes.
        """
        return self.addr[-6:]

    @classmethod
    def from_mnemonic(cls, m: str) -> "BasicAccount":
        """Takes the string of 25 words (the mnemonic) and returns the BasicAccount"""
        return cls(mnemonic.to_private_key(m))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, (BasicAccount)):
            return False
        return self._sk == other._sk and self._addr == other._addr

    def __repr__(self) -> str:
        return f"BasicAlgoAccount.\n  addr: {self.addr}\n  sk: {self.sk}"


class MultisigAccount:
    """Represents exactly the information to create
    the public address of a multisig account: the version,
    threshold and the ordered list of public addresses in the account.
    The MultiSigAccount is not meant to change. Unlike a BasicAccount,
    it does not store private information and can be entirely public.

    This is different from a algosdk.futures.transaction.Multisig,
    which stores the latest  signatures it knows about in its ordered
    list of MultisigSubsigs. Using the same Multisig for multiple
    transactions will result in errors.

    Args:
        version (int): currently, the version is 1
        threshold (int): how many signatures are necessary
        addresses (str[]): addresses in the multisig account

    Attributes:
        version (int)
        threshold (int)
        addresses (PublicAddress)
    """

    def __init__(self, version: int, threshold: int, addresses: List[str]):  #
        self.version = version
        self.threshold = threshold
        self.addresses: List[str] = list(addresses)
        self.validate()

    def validate(self) -> None:
        """Check if the account is valid by piggybacking on multiSig.validate"""
        msig = Multisig(
            version=self.version, threshold=self.threshold, addresses=self.addresses
        )
        msig.validate()

    def address(self) -> str:
        """Return the account address, again piggybacking on multiSig"""
        msig = Multisig(
            version=self.version, threshold=self.threshold, addresses=self.addresses
        )
        return str(msig.address())

    @cached_property
    def address_as_bytes(self) -> bytes:
        return encoding.decode_address(self.addr)  # type: ignore[no-any-return]

    @no_type_check
    def __eq__(self, other):
        if not isinstance(other, (MultisigAccount)):
            return False
        return (
            self.version == other.version
            and self.threshold == other.threshold
            and self.addresses == other.addresses
        )

    @cached_property
    def addr(self) -> str:
        """Return the MultisigAccount address, again piggybacking on multiSig"""
        msig = Multisig(
            version=self.version, threshold=self.threshold, addresses=self.addresses
        )
        return str(msig.address())

    @cached_property
    def addr_short_hand(self) -> str:
        """Returns the last 6 characters of the account address.

        This is just used for logging messages and human eyes!
        """
        return self.address()[-6:]

    def create_mtx(self, txn: transaction) -> MultisigTransaction:
        """Returns the MultisigTransaction for this MultisigAccount"""
        msig = Multisig(
            version=self.version, threshold=self.threshold, addresses=self.addresses
        )
        return MultisigTransaction(txn, msig)

    def __repr__(self) -> str:
        return f"MultisigAccount.\n  version {self.version}, threshold {self.threshold} \n addresses: {self.addresses}"


class PendingTxnResponse:
    """Parses the dict object of a transaction response into a Python class"""

    def __init__(self, tx_id: str, response: Dict[str, Any]) -> None:
        self.tx_id = tx_id
        self.pool_error: str = response["pool-error"]
        self.txn: Dict[str, Any] = response["txn"]

        self.application_idx: Optional[int] = response.get("application-index")
        self.asset_idx: Optional[int] = response.get("asset-index")
        self.close_rewards: Optional[int] = response.get("close-rewards")
        self.closing_amount: Optional[int] = response.get("closing-amount")
        self.confirmed_round: Optional[int] = response.get("confirmed-round")
        self.global_state_delta: Optional[Any] = response.get("global-state-delta")
        self.local_state_delta: Optional[Any] = response.get("local-state-delta")
        self.receiver_rewards: Optional[int] = response.get("receiver-rewards")
        self.sender_rewards: Optional[int] = response.get("sender-rewards")

        self.inner_txns: List[Any] = response.get("inner-txns", [])
        self.logs: List[bytes] = [base64.b64decode(l) for l in response.get("logs", [])]

    def __repr__(self) -> str:
        r = f"PendingTxnResponse: txid ..{self.tx_id[-6:]}\n"
        if self.asset_idx:
            r += f"     asset_index: {self.asset_idx}\n"
        if self.txn:
            r += f"     txn: {self.txn}\n"
        return r


def wait_for_transaction(
    client: AlgodClient, tx_id: str, timeout: int = 10
) -> PendingTxnResponse:
    """Translates algosdk client.pending_transaction_info into a Python class
    object PendingTxnResponse after waiting for a confirmed transaction

    Args:
      tx_id (str): id of transaction
      timeout (int): rounds to repeat before raising an error and giving up

    Raises:
        Exception if transaction is not confirmed in timeout rounds
    """
    last_status = client.status()
    last_round = last_status["last-round"]
    start_round = last_round

    while last_round < start_round + timeout:
        pending_txn = client.pending_transaction_info(tx_id)

        if pending_txn.get("confirmed-round", 0) > 0:
            return PendingTxnResponse(tx_id, pending_txn)

        if pending_txn["pool-error"]:
            raise Exception("Pool error: {}".format(pending_txn["pool-error"]))

        last_status = client.status_after_block(last_round + 1)

        last_round += 1

    raise Exception(f"Transaction {tx_id} not confirmed after {timeout} rounds")


def send_signed_mtx(
    client: AlgodClient, mtx: MultisigTransaction
) -> PendingTxnResponse:
    """
    Combines sending a Multisig transaction (sing send_raw_transaction)
    with waiting for the transaction to complete, returning a python
    PendingTxnResponse class object with the response.
    """
    txid = client.send_raw_transaction(encoding.msgpack_encode(mtx))
    LOGGER.info(f"Sent mtx w txid {txid[-6:]}. Waiting for confirmation")
    return wait_for_transaction(client, txid)


def pay_account(
    client: AlgodClient, sender: BasicAccount, to_addr: str, amt_in_micros: int
) -> PendingTxnResponse:
    """
    Sends micro algos from one account to another, and waits to

    Args:
        client: AlgodClient
        sender: algo_utils.BasicAccount (not algo_utils.MultisigAccount)
        to_addr (str): public address receiving the algos
        amtInMicros (int): Algos * 10**6 getting sent

    Raises:
        errors.AlgoError: raises error if fails to send, if there is a txid discrepancy

    Returns: PendingTxnResponse
    """
    if not isinstance(sender, BasicAccount):
        raise errors.AlgoError(f"Requires sender type BasicAccount, not {type(sender)}")
    txn = transaction.PaymentTxn(
        sender=sender.address(),
        receiver=to_addr,
        amt=amt_in_micros,
        sp=client.suggested_params(),
    )
    signed_txn = txn.sign(sender.sk)

    try:
        tx_id = client.send_transaction(signed_txn)
    except:
        raise errors.AlgoError(f"Failure sending transaction")
    # Interestingly, the following will occasionally throw an error
    # if txID != signedTxn.get_txid():
    #     raise errors.AlgoError(
    #         f"client.send_transaction returned different txid {txID} than SignedTransaction.get_txid() {signedTxn.get_txid()}"
    #     )
    LOGGER.info(
        f" ..{sender.addr_short_hand} sending payment of {amt_in_micros/10**6}"
        f" algos to ..{to_addr[-6:]} \n txID: ..{tx_id[-6:]}"
    )
    r = wait_for_transaction(client, signed_txn.get_txid())
    LOGGER.info(f"Got response for payAccount transaction ..{tx_id[-6:]}")
    return r


##############################################################
# SDK helpers
##############################################################


def get_balances(client: AlgodClient, addr: str) -> Dict[int, int]:
    """
    Returns a dictionary of Algorand Standard Asset holdings

    Args:
        addr (str): public address holding the ASAs

    Returns:
       A dictionary taking the ids of the held ASAs to the amounts
       of those ASAs held by the address.

    """
    balances: Dict[int, int] = dict()
    try:
        property_format.check_is_algo_address_string_format(addr)
    except:
        raise errors.AlgoError(f"addr does not have AlgoAddressStringFormat: {addr}")
    account_info = client.account_info(addr)

    # set key 0 to Algo balance
    balances[0] = account_info["amount"]

    assets: List[Dict[str, Any]] = account_info.get("assets", [])
    for asset_holding in assets:
        asset_id = asset_holding["asset-id"]
        amount = asset_holding["amount"]
        balances[asset_id] = amount

    return balances


def get_last_block_timestamp(client: AlgodClient) -> Tuple[int, int]:
    status = client.status()
    lastRound = status["last-round"]
    block = client.block_info(lastRound)
    timestamp = block["block"]["ts"]

    return block, timestamp


def micro_algos(addr: str) -> Optional[int]:
    """
    Args: acct (AlgoAccount): can also be a multiSig

    Returns:
        Optional[int]: Return the number of microAlgos in an account, or None
        if there is an issue getting this number
    """
    property_format.check_is_algo_address_string_format(addr)
    settings = gw_config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    try:
        microAlgoBalance: int = int(client.account_info(addr)["amount"])
    except:
        return None
    return microAlgoBalance


def algos(addr: str) -> Optional[float]:
    """
    Args:
      acct (AlgoAccount): can also be a multiSig

    Returns:
        Optional[int]: Return the number of microAlgos in an account, or None
        if there is an issue getting this number
    """
    property_format.check_is_algo_address_string_format(addr)
    settings = gw_config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    try:
        microAlgoBalance: int = int(client.account_info(addr)["amount"])
    except:
        return None
    return round(microAlgoBalance / 10**6, 2)


def verify_account_exists_and_funded(addr: str) -> None:
    """
    Raises an exception if an address is not a valid format, or
    if the account does not have at least 1 Algo. Note that
    every account on Algorand must have a minimum balance of
    100,000 microAlgos and this minimum balance increases with
    more holdings.

    Args:
        addr(str): the Algorand public address in question

    Raises:
        errors.AlgoError: if addr does not have AlgoAddressStringFormat, or does not have at least 1 Algo.

    """
    try:
        property_format.check_is_algo_address_string_format(addr)
    except:
        raise errors.AlgoError(
            f"In verifyAccountExistsAndFunded. address {addr} does not have valid algo address format!"
        )

    algoBalance = algos(addr)
    if algoBalance is None:
        raise errors.AlgoError(
            f"Check access to the block chain exists and that account"
            f" {addr[-6:]} is funded with min requirement (some fraction of anAlgo)"
        )
    if algoBalance < 1:
        raise errors.AlgoError(
            f"Insufficient funds for account ..{addr[-6:]}. Need 1 Algo"
            f" and only have {algoBalance}"
        )
