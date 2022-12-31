import logging
from random import choice
from typing import List
from typing import Optional

import dotenv
import gnf.algo_utils as algo_utils
import gnf.config as config
from algosdk.kmd import KMDClient
from algosdk.v2client.algod import AlgodClient
from gnf.algo_utils import BasicAccount
from gnf.algo_utils import PendingTxnResponse
from gnf.algo_utils import get_kmd_client
from gnf.algo_utils import pay_account
from gnf.errors import AlgoError


FUNDING_AMOUNT = 1_000_000


DEV_DEMO_HOLLY_SK = "sp4SDWmH8Rin0IhPJQq1UMsSR5C0j1IGqzLdcwCMySBVzT8lEUwjwwpS9z6l6dKSg52WWEjRdJDAL+eVt4kvBg=="
DEV_DEMO_MOLLY_SK = "FCLmrvflibLD6Deu3NNiUQCC9LOWpXLsbMR/cP2oJzH8IT4Zu8vBAhRNsXoWF+2i6q2KyBZrPhmbDCKJD7rBBg=="

JOINT_ACCOUNT_SIGNING_THRESHOLD = 2


kmdAccounts: Optional[List[BasicAccount]] = None
LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


def dev_fund_to_min(addr: str, min_algos: int):
    if algo_utils.algos(addr) is None:
        dev_fund_account(
            config.VanillaSettings(_env_file=dotenv.find_dotenv()),
            to_addr=addr,
            amt_in_micros=min_algos * 10**6,
        )
    elif algo_utils.algos(addr) < min_algos:
        dev_fund_account(
            config.VanillaSettings(_env_file=dotenv.find_dotenv()),
            to_addr=addr,
            amt_in_micros=min_algos * 10**6,
        )


def dev_fund_account(
    settings: config.VanillaSettings,
    to_addr: str,
    amt_in_micros: int = FUNDING_AMOUNT,
) -> PendingTxnResponse:
    """Funds an adddress in local sandbox mode using a randomly chosen genesis
    account.
    Args:
        settingsAlgo (config.Algo): has the kmd wallet for the genesis accounts
        toAddr (str): address receiving the money
        microAlgoAmount (int, optional):  Defaults to FUNDING_AMOUNT.

    Returns: PendingTxnResponse
    """
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


def dev_fund_admin_and_graveyard(settings: config.VanillaSettings):
    """Fund admin account from one of the sandbox
    genesis accounts. Only for the dev universe"""
    admin_addr = settings.public.gnf_admin_addr
    graveyard_addr = settings.public.gnf_graveyard_addr
    if algo_utils.micro_algos(admin_addr) < 1:
        dev_fund_account(settings=settings, to_addr=admin_addr)
    LOGGER.info(
        f"gnf admin account balance: {algo_utils.micro_algos(admin_addr)} microAlgos"
    )
    if algo_utils.micro_algos(graveyard_addr) < 1:
        dev_fund_account(settings=settings, to_addr=graveyard_addr)
    LOGGER.info(
        f"gnf graveyard account balance: {algo_utils.micro_algos(graveyard_addr)} microAlgos"
    )
