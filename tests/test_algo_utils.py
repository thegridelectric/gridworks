import algosdk
import dotenv
import pytest
from algosdk.v2client.algod import AlgodClient

import gridworks.algo_utils as algo_utils
import gridworks.dev_utils.algo_setup as algo_setup
import gridworks.gw_config as config
from gridworks.errors import AlgoError


@pytest.mark.skip(reason="Skipped so a package can be published")
def test_pay_account():
    algo_settings = config.GnfPublic()
    addr0: str = algo_settings.gnf_admin_addr
    validator_sk = config.ValidatorSettings().sk.get_secret_value()
    molly_acct = algo_utils.BasicAccount(private_key=validator_sk)
    addr1: str = molly_acct.addr
    addresses = [addr0, addr1]
    multi = algo_utils.MultisigAccount(version=1, threshold=2, addresses=addresses)

    initial_balance = algo_utils.micro_algos(multi.addr)
    # This is the test of payAccount working, called by devFundAccount which grabs
    # a genesis BasicAccount
    r = algo_setup.dev_fund_account(
        settings=config.VanillaSettings(_env_file=dotenv.find_dotenv()),
        to_addr=multi.addr,
        amt_in_micros=200_000,
    )
    assert isinstance(r, algo_utils.PendingTxnResponse)
    assert algo_utils.micro_algos(multi.addr) >= initial_balance + 200_000

    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )

    # MultisigAccount attempts to pay a BasicAccount. But a MultisigAccount does not
    # contain the private signing keys of its component addresses, so this will fail.

    with pytest.raises(AlgoError):
        algo_utils.pay_account(
            client=client, sender=multi, to_addr=addr1, amt_in_micros=100_000
        )


def test_basic_account():
    testAcct = algosdk.account.generate_account()

    acct: algo_utils.BasicAccount = algo_utils.BasicAccount(private_key=testAcct[0])

    assert acct.addr == testAcct[1]
    assert acct.sk == testAcct[0]

    acct: algo_utils.BasicAccount = algo_utils.BasicAccount()

    assert acct.addr == acct.address()
    assert acct.sk == acct.private_key()
    assert acct.address_as_bytes == algosdk.encoding.decode_address(acct.addr)
    assert acct.mnemonic == algosdk.mnemonic.from_private_key(acct.sk)
    assert acct.from_mnemonic(acct.mnemonic) == acct
    assert acct.__repr__() is not None
    assert acct.addr_short_hand == acct.addr[-6:]


def test_multisig_account():
    acct0: algo_utils.BasicAccount = algo_utils.BasicAccount()
    acct1: algo_utils.BasicAccount = algo_utils.BasicAccount()
    addresses = [acct0.addr, acct1.addr]

    with pytest.raises(Exception):
        m = algo_utils.MultisigAccount(
            version=1, threshold=0, addresses=["Hello", "World"]
        )
    with pytest.raises(algosdk.error.InvalidThresholdError):
        m = algo_utils.MultisigAccount(version=1, threshold=0, addresses=addresses)

    with pytest.raises(algosdk.error.InvalidThresholdError):
        m = algo_utils.MultisigAccount(version=1, threshold=3, addresses=addresses)

    multi = algo_utils.MultisigAccount(version=1, threshold=2, addresses=addresses)
    msig = algosdk.future.transaction.Multisig(
        version=1, threshold=2, addresses=addresses
    )

    assert multi.addresses == addresses

    acct2 = algo_utils.BasicAccount()
    addresses.append(acct2.addr)
    # multi grabs a copy of the list of addresses. If the original list changes,
    # multi keeps the original
    assert multi.addresses == [acct0.addr, acct1.addr]

    assert multi.address() == msig.address()

    assert multi.addr == multi.address()
    assert multi.addr_short_hand == multi.addr[-6:]

    subsig0: algosdk.future.transaction.MultisigSubsig = msig.subsigs[0]
    assert subsig0.public_key == acct0.address_as_bytes

    assert multi.__repr__() is not None
