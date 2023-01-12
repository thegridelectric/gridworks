import logging
from random import choice
from typing import List
from typing import Optional

import dotenv
from algosdk.kmd import KMDClient
from algosdk.v2client.algod import AlgodClient

import gridworks.algo_utils as algo_utils
import gridworks.gw_config as config
from gridworks.algo_utils import BasicAccount
from gridworks.algo_utils import PendingTxnResponse
from gridworks.algo_utils import get_kmd_client
from gridworks.algo_utils import pay_account
from gridworks.errors import AlgoError


FUNDING_AMOUNT = 1_000_000


kmdAccounts: Optional[List[BasicAccount]] = None
LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


def dev_fund_to_min(addr: str, min_algos: int) -> PendingTxnResponse:
    """
    Tops up the AlgoAddr so that it has at least min_algos Algos, using a randomly
    chosen genesis acct from the sandbox. Note that the native algosdk pay_account
    uses micro Algos (in ints).

    Returns: PendingTxnResponse
    """
    if algo_utils.algos(addr) is None:
        return dev_fund_account(
            config.VanillaSettings(_env_file=dotenv.find_dotenv()),
            to_addr=addr,
            amt_in_micros=int(min_algos * 10**6),
        )
    elif algo_utils.algos(addr) < min_algos:
        return dev_fund_account(
            config.VanillaSettings(_env_file=dotenv.find_dotenv()),
            to_addr=addr,
            amt_in_micros=int((min_algos - algo_utils.algos(addr)) * 10**6),
        )


def dev_fund_account(
    settings: config.VanillaSettings,
    to_addr: str,
    amt_in_micros: int = FUNDING_AMOUNT,
) -> PendingTxnResponse:
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )

    fundingAccount = choice(dev_get_genesis_accounts(settings))
    return pay_account(
        client=client,
        sender=fundingAccount,
        to_addr=to_addr,
        amt_in_micros=amt_in_micros,
    )


def dev_get_genesis_accounts(
    settings: config.VanillaSettings,
) -> List[BasicAccount]:
    global kmdAccounts

    if kmdAccounts is None:
        kmd: KMDClient = get_kmd_client(settings)

        try:
            wallets = kmd.list_wallets()
        except:
            raise AlgoError(
                "Algo key management demon failed to connect to chain. Check blockchain access"
            )
        walletID = None
        walletName = settings.public.gen_kmd_wallet_name
        for wallet in wallets:
            if wallet["name"] == walletName:
                walletID = wallet["id"]
                break

        if walletID is None:
            raise Exception("Wallet not found: {walletName}")

        walletPassword = (
            settings.algo_api_secrets.gen_kmd_wallet_password.get_secret_value()
        )
        walletHandle = kmd.init_wallet_handle(walletID, walletPassword)
        try:
            addresses = kmd.list_keys(walletHandle)
            privateKeys = [
                kmd.export_key(walletHandle, walletPassword, addr) for addr in addresses
            ]
            kmdAccounts = [BasicAccount(sk) for sk in privateKeys]
        finally:
            kmd.release_wallet_handle(walletHandle)
        LOGGER.debug(f"Found {len(kmdAccounts)} genesis accounts in {walletName}")
    return kmdAccounts
