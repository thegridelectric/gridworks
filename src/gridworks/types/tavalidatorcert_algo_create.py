"""Type tavalidatorcert.algo.create, version 000"""
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


class TavalidatorcertAlgoCreate(BaseModel):
    """Used for Step 1 of TaValidator certification.

    Meant to be sent from a pending TaValidator  to the GNodeFactory (Gnf), to
    initiate the process of certifying the pending TaValidator.
    [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html).
    """

    ValidatorAddr: str = Field(
        title="The address of the pending TaValidator",
    )
    HalfSignedCertCreationMtx: str = Field(
        title="Algo multi-transaction for certificate creation, with 1 of 2 signatures",
    )
    TypeName: Literal["tavalidatorcert.algo.create"] = "tavalidatorcert.algo.create"
    Version: str = "000"

    @validator("ValidatorAddr")
    def check_validator_addr(cls, v: str) -> str:
        """
        Axiom 5: Uniqueness.
        There must not already be a TaValidatorCert belonging to the  2-sig [GnfAdminAddr, ValidatorAddr] address.
        """
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"ValidatorAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        raise NotImplementedError("Implement axiom(s)")
        return v

    @validator("HalfSignedCertCreationMtx")
    def check_half_signed_cert_creation_mtx(cls, v: str) -> str:
        """
        Axioms 2, 3:

        Axiom 2: Is AssetCreateTxn.
        The transaction must have type AssetCreateTxn.

        Axiom 3: Is ValidatorCert.
        For the asset getting created: Total is 1, Decimals is 0, UnitName is VLDTR, Manager is GnfAdminAddr,
        AssetName is not blank.
        [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html#tavalidator-certificate)
        """
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"HalfSignedCertCreationMtx failed AlgoMsgPackEncoded format validation: {e}"
            )
        raise NotImplementedError("Implement axiom(s)")
        return v

    @root_validator(pre=True)
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Is correct Multisig.
        Decoded HalfSignedCertCreationMtx must have type MultisigTransaction from the
        2-sig MultiAccount  [GnfAdminAddr, ValidatorAddr], signed by ValidatorAddr.
        [More info](https://gridworks.readthedocs.io/en/latest/g-node-factory.html#gnfadminaddr)
        """
        raise NotImplementedError("Implement check for axiom 1")

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class TavalidatorcertAlgoCreate_Maker:
    type_name = "tavalidatorcert.algo.create"
    version = "000"

    def __init__(self, validator_addr: str, half_signed_cert_creation_mtx: str):
        self.tuple = TavalidatorcertAlgoCreate(
            ValidatorAddr=validator_addr,
            HalfSignedCertCreationMtx=half_signed_cert_creation_mtx,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: TavalidatorcertAlgoCreate) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> TavalidatorcertAlgoCreate:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> TavalidatorcertAlgoCreate:
        d2 = dict(d)
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "HalfSignedCertCreationMtx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HalfSignedCertCreationMtx")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return TavalidatorcertAlgoCreate(
            ValidatorAddr=d2["ValidatorAddr"],
            HalfSignedCertCreationMtx=d2["HalfSignedCertCreationMtx"],
            TypeName=d2["TypeName"],
            Version="000",
        )
