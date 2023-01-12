"""Type initial.tadeed.algo.create, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gridworks.errors import SchemaError


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


class InitialTadeedAlgoCreate(BaseModel):
    """TaValidator sends to GNodeFactory to complete creation of an initial TaDeed.

    If this message is valid, the GNodeFactory co-signs and submits the TaDeed creation. In addition, the
    GnodeFactory creates a TerminalAsset with GNodeStatus pending.  For more information:
    [TaDeed](https://gridworks.readthedocs.io/en/latest/ta-deed.html)
    [TaValidator](https://gridworks.readthedocs.io/en/latest/ta-validator.html)
    """

    ValidatorAddr: str = Field(
        title="Address of the TaValidator",
        description="The Algorand address of the TaValidator who is going to validate the location, device type, and power metering of the TerminalAsset.",
    )
    HalfSignedDeedCreationMtx: str = Field(
        title="Algo mulit-transaction for TaDeed creation",
    )
    TypeName: Literal["initial.tadeed.algo.create"] = "initial.tadeed.algo.create"
    Version: str = "000"

    @validator("ValidatorAddr")
    def _check_validator_addr(cls, v: str) -> str:
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"ValidatorAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("HalfSignedDeedCreationMtx")
    def _check_half_signed_deed_creation_mtx(cls, v: str) -> str:
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"HalfSignedDeedCreationMtx failed AlgoMsgPackEncoded format validation: {e}"
            )
        return v

    @root_validator(pre=True)
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Is correct Multisig.
        Decoded HalfSignedDeedCreationMtx must have type MultisigTransaction from the
        2-sig MultiAccount  [GnfAdminAddr, ValidatorAddr].
        [More info](https://gridworks.readthedocs.io/en/latest/g-node-factory.html#gnfadminaddr)
        """
        raise NotImplementedError("Implement check for axiom 1")

    @root_validator
    def check_axiom_2(cls, v: dict) -> dict:
        """
        Axiom 2: Creates Initial ASA TaDeed.
        The transaction must create an Algorand Standard Asset
           - Total is 1
           - UnitName is TADEED
           - Manager is GnfAdminAddr
           - AssetName has the following characteristics:
                 - length <=  32 characters
                 - LeftRightDot format
                 - final word is '.ta'
        [More info](https://gridworks.readthedocs.io/en/latest/ta-deed.html#asa-tadeed-specs)
        """
        raise NotImplementedError("Implement check for axiom 2")

    @root_validator
    def check_axiom_3(cls, v: dict) -> dict:
        """
        Axiom 3: Mtx signed by TaValidator.

        """
        raise NotImplementedError("Implement check for axiom 3")

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class InitialTadeedAlgoCreate_Maker:
    type_name = "initial.tadeed.algo.create"
    version = "000"

    def __init__(self, validator_addr: str, half_signed_deed_creation_mtx: str):
        self.tuple = InitialTadeedAlgoCreate(
            ValidatorAddr=validator_addr,
            HalfSignedDeedCreationMtx=half_signed_deed_creation_mtx,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: InitialTadeedAlgoCreate) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> InitialTadeedAlgoCreate:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> InitialTadeedAlgoCreate:
        d2 = dict(d)
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "HalfSignedDeedCreationMtx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HalfSignedDeedCreationMtx")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return InitialTadeedAlgoCreate(
            ValidatorAddr=d2["ValidatorAddr"],
            HalfSignedDeedCreationMtx=d2["HalfSignedDeedCreationMtx"],
            TypeName=d2["TypeName"],
            Version="000",
        )
