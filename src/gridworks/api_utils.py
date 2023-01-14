"""Helpers for working with GridWorks specific Algorand certificates and Smart
Contracts. Heavily used in API Type validation. """

from typing import Optional

import dotenv
from algosdk import encoding
from algosdk.future.transaction import MultisigTransaction
from algosdk.v2client.algod import AlgodClient
from pydantic import BaseModel

import gridworks.algo_utils as algo_utils
import gridworks.gw_config as config
import gridworks.property_format as property_format
from gridworks.enums import AlgoCertType
from gridworks.errors import SchemaError
from gridworks.types import GwCertId


def get_discoverer_account_with_admin(
    discoverer_addr: str,
) -> algo_utils.MultisigAccount:
    """
    Returns the 2-sig multi [discoverer, gnf_admin_addr]
    address for a GridWorks Discoverer.

    :param str discoverer_addr: The Algorand address of the Discoverer
    :raise Exception SchemaError: Returned if discoverer_addr has wrong format.
    """
    try:
        property_format.check_is_algo_address_string_format(discoverer_addr)
    except SchemaError:
        raise SchemaError(
            f"getValidatorAccountWithAdmin called with validatorAddr not of AlgoAddressStringFormat: \n{discoverer_addr}"
        )

    return algo_utils.MultisigAccount(
        version=1,
        threshold=2,
        addresses=[discoverer_addr, config.Public().gnf_admin_addr],
    )


def get_validator_account_with_admin(
    validator_addr: str,
) -> algo_utils.MultisigAccount:
    """
    Returns the 2-sig multi [gnf_admin_addr, validator_addr]
    address for a GridWorks Validator.

    :param str validator_addr: The Algorand address of the Discoverer
    :raise Exception SchemaError: Returned if discoverer_addr has wrong format.
    """
    try:
        property_format.check_is_algo_address_string_format(validator_addr)
    except SchemaError:
        raise SchemaError(
            f"getValidatorAccountWithAdmin called with validatorAddr not of AlgoAddressStringFormat: \n{validator_addr}"
        )

    return algo_utils.MultisigAccount(
        version=1,
        threshold=2,
        addresses=[config.Public().gnf_admin_addr, validator_addr],
    )


def check_validator_multi_has_enough_algos(ta_validator_addr: str) -> None:
    """
    Raises exception if the 2-sig multi [GNfAdminAddr, ta_validator_addr] insufficiently funded.
    Set publicly by the GNodeFactory.
    [More info](https://gridworks.readthedocs.io/en/latest/g-node-factory.html#tavalidatorfundingthresholdalgos)

    Args:
        validator_addr: the public address of the pending validator

    Raises:
        SchemaError if joint account does not have Public().gnf_validator_funding_threshold_algos.
    """
    try:
        property_format.check_is_algo_address_string_format(ta_validator_addr)
    except SchemaError:
        raise Exception(
            f"called with ta_validator_addr not of AlgoAddressStringFormat: \n{ta_validator_addr}"
        )
    min_algos = config.Public().ta_validator_funding_threshold_algos
    multi: algo_utils.MultisigAccount = get_validator_account_with_admin(
        ta_validator_addr
    )
    if algo_utils.algos(multi.addr) is None:
        raise SchemaError(
            f"multi  ..{multi.addr[-6:]}  for validator ..{ta_validator_addr[-6:]} is unfunded. Requires {min_algos} Algos."
        )
    if algo_utils.algos(multi.addr) < min_algos:
        raise SchemaError(
            f"multi  ..{multi.addr[-6:]}  for validator ..{ta_validator_addr[-6:]} has {algo_utils.algos(multi.addr)} Algos. Requires {min_algos} Algos. "
        )


def check_mtx_subsig(mtx: MultisigTransaction, signer_addr) -> None:
    """Throws a SchemaError if the signer_addr is not a signer for mtx or did not sign.
    TODO: add error if the signature does not match the txn.
    """
    signer_pk = encoding.decode_address(signer_addr)
    sig_by_public_key = {}
    for subsig in mtx.multisig.subsigs:
        sig_by_public_key[subsig.public_key] = subsig.signature

    if not signer_pk in sig_by_public_key.keys():
        raise SchemaError(
            f"signer_addr ..{signer_addr[-6:]} not a signer for multisig!!"
        )
    if sig_by_public_key[signer_pk] is None:
        raise SchemaError(f"signer_addr ..{signer_addr[-6:]} did not sign!")
    # TODO: check that the signature is for THIS transaction


def get_validator_cert_idx(validator_addr: str) -> Optional[int]:
    """
    Looks for an asset in the validatorMsig account that is a
    validator certificate (based on unit name).
    [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html#tavalidator-certificate)

    Args:
        validator_addr: the public address of the validator (NOT the multi)

    Returns:
        Optional[int]: returns None if no Validator Certificate is found,
        otherwise the unique  identifier of the certificate. Since
        Validator certificates are always ASA, this identifier is an int.
    """
    multi: algo_utils.MultisigAccount = get_validator_account_with_admin(validator_addr)
    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    try:
        created_assets = client.account_info(multi.addr)["created-assets"]
    except:
        return None
    certs = list(filter(lambda x: x["params"]["unit-name"] == "VLDTR", created_assets))
    if len(certs) == 0:
        return None
    else:
        return certs[0]["index"]


def is_ta_validator(acct_addr: str) -> bool:
    """
    Returns True if the account_addr is the TaValidatorAddr  for a TaValidator
    False otherwise
    [more info](https://gridworks.readthedocs.io/en/latest/ta-validator.html)
    """
    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    cert_asset_idx = get_validator_cert_idx(acct_addr)
    if cert_asset_idx is None:
        return False

    asset_dicts = client.account_info(acct_addr)["assets"]
    opt_in_ids = list(map(lambda x: x["asset-id"], asset_dicts))
    if cert_asset_idx not in opt_in_ids:
        return False
    our_dict = list(filter(lambda x: x["asset-id"] == cert_asset_idx, asset_dicts))[0]
    if our_dict["amount"] == 0:
        return False
    return True


def get_tatrading_rights_id(terminal_asset_alias: str) -> Optional[GwCertId]:
    """
    Returns unique identifier for TaTradingRights
    [more info](https://gridworks.readthedocs.io/en/latest/ta-trading-rights.html#tatradingrights-technical-details)
    [GwCertId.Type](https://gridworks.readthedocs.io/en/latest/enums.html#gridworks.enums.AlgoCertType)

    Args:
        terminal_asset_alias (str): The GNodeAlias of the TerminalAsset that
        the TaTradingRights are for

    Returns:
        Optional[GwCertId]: returns None if no TaTradingRights
        are found. Otherwise returns the unique identifier of the TaTradingRights,
        which is an AlgoAddress string if the GwCertId.Type==SmartSig, and is
        an integer if the GwCertId.Type==ASA
    """
    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    try:
        created_assets = client.account_info(settings.public.gnf_admin_addr)[
            "created-assets"
        ]
    except:
        return None
    # Look through ASA-type TaTradingRights
    ta_trading_rights = list(
        filter(lambda x: x["params"]["unit-name"] == "TATRADE", created_assets)
    )
    this_ta_trading_rights = list(
        filter(lambda x: x["params"]["name"] == terminal_asset_alias, ta_trading_rights)
    )
    if len(this_ta_trading_rights) == 0:
        return None
    else:
        return GwCertId(
            Type=AlgoCertType.ASA,
            Idx=this_ta_trading_rights[0]["index"],
        )


def get_tadeed_id(terminal_asset_alias: str, validator_addr: str) -> Optional[GwCertId]:
    """Looks for an asset created in the 2-sig [Gnf Admin, validator_addr] account
     that is a tadeed for terminal_asset_alias.
    [more info](https://gridworks.readthedocs.io/en/latest/ta-deed.html#tadeed-technical-details)
    [GwCertId.Type](https://gridworks.readthedocs.io/en/latest/enums.html#gridworks.enums.AlgoCertType)

    Args:
        terminal_asset_alias (str): the alias of the Terminal Asset
        validator_addr (str): the AlgoAddress of the Validator

    Returns:
        Optional[GwCertId]: returns None if no TaDeed for this alias was
        created by the two-sig Multi [GnfAdminAddr, validator_addr]. Otherwise
        returns the unique identifier of the TaDeed, which is an AlgoAddress
        string if the GwCertId.Type=SmartSig, and is an integer if the GwCertId.Type=ASA
    """
    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )

    multi: algo_utils.MultisigAccount = get_validator_account_with_admin(validator_addr)
    try:
        created_assets = client.account_info(multi.addr)["created-assets"]
    except:
        return None
    ta_deeds = list(
        filter(lambda x: x["params"]["unit-name"] == "TADEED", created_assets)
    )
    this_ta_deed = list(
        filter(lambda x: x["params"]["name"] == terminal_asset_alias, ta_deeds)
    )
    if len(this_ta_deed) == 0:
        # TODO: look through SmartSigs
        return None
    else:
        return GwCertId(
            Type=AlgoCertType.ASA,
            Idx=this_ta_deed[0]["index"],
        )


def is_ta_deed(asset_idx: int) -> bool:
    """
    Returns True if the asset_idx is the unique identifier for a TaDeed
    certificate. Note that the AlgoCertType must be ASA
    [more info](https://gridworks.readthedocs.io/en/latest/ta-deed.html#tadeed-technical-details)

    Args:
        asset_idx(int): the ASA id in question
    """
    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    try:
        info = client.asset_info(asset_idx)
    except:
        return False
    try:
        unit_name = info["params"]["unit-name"]
    except:
        return False
    if unit_name != "TADEED":
        return False
    if info["params"]["total"] != 1:
        return False
    if info["manager"] != settings.public.gnf_admin_addr:
        return False
    # TODO: add check that creator was a 2-sig multi with first addr GnfAdminAddr
    if not property_format.is_left_right_dot(info["params"]["name"]):
        return False
    return True


def alias_from_deed_idx(asset_idx: int) -> Optional[str]:
    """
    Returns the TerminalAsset's GNodeAlias from the the TaDeed
    unique identifer (when the AlgoCertType is ASA, and the identifier
    is an integer). Returns None if the asset_idx is not in fact
    the identifier for a TaDeed
    [more info](https://gridworks.readthedocs.io/en/latest/ta-deed.html#tadeed)

    Args:
        asset_idx(int): the ASA id in question
    """
    if not is_ta_deed(asset_idx):
        return None
    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    info = client.asset_info(asset_idx)
    return info["params"]["name"]


def is_validator_addr(validator_addr: str) -> bool:
    """
    Checks if Validator Multi has a single valid TaValidator certificate
    """
    settings = config.VanillaSettings(_env_file=dotenv.find_dotenv())
    client: AlgodClient = AlgodClient(
        settings.algo_api_secrets.algod_token.get_secret_value(),
        settings.public.algod_address,
    )
    multi = get_validator_account_with_admin(validator_addr)
    try:
        created_assets = client.account_info(multi.addr)["created-assets"]
    except:
        return False
    validator_certs = list(
        filter(lambda x: x["params"]["unit-name"] == "VLDTR", created_assets)
    )
    if len(validator_certs) != 1:
        return False
    params = validator_certs[0]["params"]
    if params["total"] != 1:
        return False
    if params["decimals"] != 0:
        return False
    if "name" not in params.keys():
        return False
    if params["name"] == "":
        return False
    if params["manager"] != settings.public.gnf_admin_addr:
        return False
    if params["creator"] != multi.addr:
        return False
    return True
