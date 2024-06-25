"""Type gw.cert.id, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from gridworks.enums import GwStrEnum
from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gridworks.enums import AlgoCertType
from gridworks.errors import SchemaError
from gridworks.message import as_enum


class AlgoCertType000SchemaEnum:
    enum_name: str = "algo.cert.type.000"
    symbols: List[str] = [
        "00000000",
        "086b5165",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class AlgoCertType000(GwStrEnum):
    ASA = auto()
    SmartSig = auto()

    @classmethod
    def default(cls) -> "AlgoCertType000":
        return cls.ASA

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class AlgoCertTypeMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> AlgoCertType:
        if not AlgoCertType000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to AlgoCertType000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, AlgoCertType, AlgoCertType.default())

    @classmethod
    def local_to_type(cls, algo_cert_type: AlgoCertType) -> str:
        if not isinstance(algo_cert_type, AlgoCertType):
            raise SchemaError(f"{algo_cert_type} must be of type {AlgoCertType}")
        versioned_enum = as_enum(
            algo_cert_type, AlgoCertType000, AlgoCertType000.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, AlgoCertType000] = {
        "00000000": AlgoCertType000.ASA,
        "086b5165": AlgoCertType000.SmartSig,
    }

    versioned_enum_to_type_dict: Dict[AlgoCertType000, str] = {
        AlgoCertType000.ASA: "00000000",
        AlgoCertType000.SmartSig: "086b5165",
    }


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


class GwCertId(BaseModel):
    """Clarifies whether cert id is an Algorand Standard Asset or SmartSig"""

    Type: AlgoCertType = Field(
        title="Type",
    )
    Idx: Optional[int] = Field(
        title="ASA Index",
        default=None,
    )
    Addr: Optional[str] = Field(
        title="Algorand Smart Signature Address",
        default=None,
    )
    TypeName: Literal["gw.cert.id"] = "gw.cert.id"
    Version: str = "000"

    @validator("Type")
    def _check_type(cls, v: AlgoCertType) -> AlgoCertType:
        return as_enum(v, AlgoCertType, AlgoCertType.ASA)

    @validator("Addr")
    def _check_addr(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"Addr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @root_validator
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Cert type consistency.
        If Type is ASA, then Id exists and Addr does not. Otherwise, Addr exists
        and Id does not.
        """
        Type: AlgoCertType = v.get("Type", None)
        Idx: int = v.get("Idx", None)
        Addr: str = v.get("Addr", None)

        if Type == AlgoCertType.ASA:
            if Idx is None:
                raise ValueError("If Type is ASA then Idx must exist")
            if Addr is not None:
                raise ValueError("If Type is ASA then Addr must be None")
        if Type == AlgoCertType.SmartSig:
            if Idx is not None:
                raise ValueError("If Type is SmartSig then Idx must be None")
            if Addr is None:
                raise ValueError("If Type is SmartSig then Addr must exist")
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["Type"]
        Type = as_enum(self.Type, AlgoCertType, AlgoCertType.default())
        d["TypeGtEnumSymbol"] = AlgoCertTypeMap.local_to_type(Type)
        if d["Idx"] is None:
            del d["Idx"]
        if d["Addr"] is None:
            del d["Addr"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class GwCertId_Maker:
    type_name = "gw.cert.id"
    version = "000"

    def __init__(self, type: AlgoCertType, idx: Optional[int], addr: Optional[str]):
        self.tuple = GwCertId(
            Type=type,
            Idx=idx,
            Addr=addr,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GwCertId) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GwCertId:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> GwCertId:
        d2 = dict(d)
        if "TypeGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeGtEnumSymbol")
        if d2["TypeGtEnumSymbol"] in AlgoCertType000SchemaEnum.symbols:
            d2["Type"] = AlgoCertTypeMap.type_to_local(d2["TypeGtEnumSymbol"])
        else:
            d2["Type"] = AlgoCertType.default()
        if "Idx" not in d2.keys():
            d2["Idx"] = None
        if "Addr" not in d2.keys():
            d2["Addr"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return GwCertId(
            Type=d2["Type"],
            Idx=d2["Idx"],
            Addr=d2["Addr"],
            TypeName=d2["TypeName"],
            Version="000",
        )
