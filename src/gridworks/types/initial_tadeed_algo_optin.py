"""Type initial.tadeed.algo.optin, version 002"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gridworks.errors import SchemaError


def check_is_left_right_dot(v: str) -> None:
    """
    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Raises:
        ValueError: if not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate {v} into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(f"Most significant word of {v} must start with alphabet char.")
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of {v} split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of {v} must be lowercase.")


def check_is_algo_address_string_format(v: str) -> None:
    """
    AlgoAddressStringFormat format: The public key of a private/public Ed25519
    key pair, transformed into an  Algorand address, by adding a 4-byte checksum
    to the end of the public key and then encoding in base32.

    Raises:
        ValueError: if not AlgoAddressStringFormat format
    """
    import algosdk

    at = algosdk.abi.AddressType()
    try:
        result = at.decode(at.encode(v))
    except Exception as e:
        raise ValueError(f"Not AlgoAddressStringFormat: {e}")


def check_is_algo_msg_pack_encoded(v: str) -> None:
    """
    AlgoMSgPackEncoded format: the format of an  transaction sent to
    the Algorand blockchain.

    Raises:
        ValueError: if not AlgoMSgPackEncoded  format
    """
    import algosdk

    try:
        algosdk.encoding.future_msgpack_decode(v)
    except Exception as e:
        raise ValueError(f"Not AlgoMsgPackEncoded format: {e}")


class InitialTadeedAlgoOptin(BaseModel):
    """Received by TaDaemon so that it can opt into intial TaDeed.

    The TaDaemon must opt into the TaDeed before receiving it. This message prompts that action.
    """

    TerminalAssetAlias: str = Field(
        title="The GNodeAlias of the TerminalAsset",
    )
    TaOwnerAddr: str = Field(
        title="The Algorand address of the owner for the TerminalAsset",
    )
    ValidatorAddr: str = Field(
        title="Address of the TaValidator",
        description="The Algorand address of the TaValidator who has validated the location, device type, and power metering of the TerminalAsset.",
    )
    SignedInitialDaemonFundingTxn: str = Field(
        title="SignedInitialDaemonFundingTxn",
        description="Funding transaction for the TaDaemon account, signed by the TaOwner.",
    )
    TypeName: Literal["initial.tadeed.algo.optin"] = "initial.tadeed.algo.optin"
    Version: str = "002"

    @validator("TerminalAssetAlias")
    def _check_terminal_asset_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"TerminalAssetAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("TaOwnerAddr")
    def _check_ta_owner_addr(cls, v: str) -> str:
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"TaOwnerAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("ValidatorAddr")
    def _check_validator_addr(cls, v: str) -> str:
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"ValidatorAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("SignedInitialDaemonFundingTxn")
    def _check_signed_initial_daemon_funding_txn(cls, v: str) -> str:
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"SignedInitialDaemonFundingTxn failed AlgoMsgPackEncoded format validation: {e}"
            )
        return v

    @root_validator(pre=True)
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Is correct Multisig.
        Decoded SignedInitialDaemonFundingTxn must be a SignedTransaction signed by TaOwnerAddr.
        """
        raise NotImplementedError("Implement check for axiom 1")

    @root_validator
    def check_axiom_2(cls, v: dict) -> dict:
        """
        Axiom 2: TaDeed consistency.
        There is an ASA TaDeed created by and owned by the 2-sig MultiAccount [GnfAdminAddr, ValidatorAddr],
        where the TaDeed's AssetName is equal to the payload's TerminalAssetAlias.
        """
        raise NotImplementedError("Implement check for axiom 2")

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class InitialTadeedAlgoOptin_Maker:
    type_name = "initial.tadeed.algo.optin"
    version = "002"

    def __init__(
        self,
        terminal_asset_alias: str,
        ta_owner_addr: str,
        validator_addr: str,
        signed_initial_daemon_funding_txn: str,
    ):
        self.tuple = InitialTadeedAlgoOptin(
            TerminalAssetAlias=terminal_asset_alias,
            TaOwnerAddr=ta_owner_addr,
            ValidatorAddr=validator_addr,
            SignedInitialDaemonFundingTxn=signed_initial_daemon_funding_txn,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: InitialTadeedAlgoOptin) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> InitialTadeedAlgoOptin:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> InitialTadeedAlgoOptin:
        d2 = dict(d)
        if "TerminalAssetAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TerminalAssetAlias")
        if "TaOwnerAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TaOwnerAddr")
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "SignedInitialDaemonFundingTxn" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SignedInitialDaemonFundingTxn")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return InitialTadeedAlgoOptin(
            TerminalAssetAlias=d2["TerminalAssetAlias"],
            TaOwnerAddr=d2["TaOwnerAddr"],
            ValidatorAddr=d2["ValidatorAddr"],
            SignedInitialDaemonFundingTxn=d2["SignedInitialDaemonFundingTxn"],
            TypeName=d2["TypeName"],
            Version="002",
        )
