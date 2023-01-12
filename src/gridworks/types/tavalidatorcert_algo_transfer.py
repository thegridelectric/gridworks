"""Type tavalidatorcert.algo.transfer, version 000"""
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


class TavalidatorcertAlgoTransfer(BaseModel):
    """Used for Step 2 of TaValidator certification.

    Meant to be sent from a pending TaValidator  to the GNodeFactory (Gnf), so the
    Gnf will transfer its ValidatorCert to the pending TaValidator's Algorand address.
    [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html).
    """

    ValidatorAddr: str = Field(
        title="The address of the pending TaValidator",
    )
    HalfSignedCertTransferMtx: str = Field(
        title="Algo multi-transaction for certificate transfer, with 1 of 2 signatures",
    )
    TypeName: Literal["tavalidatorcert.algo.transfer"] = "tavalidatorcert.algo.transfer"
    Version: str = "000"

    @validator("ValidatorAddr")
    def check_validator_addr(cls, v: str) -> str:
        """
        Axiom 4: TaValidator has sufficient Algos.
        ValidatorAddr must have enough Algos  to meet the GNodeFactory criterion.
        """
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"ValidatorAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        raise NotImplementedError("Implement axiom(s)")
        return v

    @validator("HalfSignedCertTransferMtx")
    def _check_half_signed_cert_transfer_mtx(cls, v: str) -> str:
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"HalfSignedCertTransferMtx failed AlgoMsgPackEncoded format validation: {e}"
            )
        return v

    @root_validator(pre=True)
    def check_axiom_1(cls, v: dict) -> dict:
        """
        Axiom 1: Is correct Multisig.
        Decoded HalfSignedCertTransferMtx must have type MultisigTransaction from the
        2-sig MultiAccount  [GnfAdminAddr, ValidatorAddr].
        [More info](https://gridworks.readthedocs.io/en/latest/g-node-factory.html#gnfadminaddr)
        """
        raise NotImplementedError("Implement check for axiom 1")

    @root_validator
    def check_axiom_2(cls, v: dict) -> dict:
        """
        Axiom 2: Transfers correct certificate.
         - The transaction must be the transfer of an Algorand Standard Asset
         - It must be getting transferred from its creator, which must be the 2-sig Multi [GnfAdmin, TaValidatorAddr]
         - It must be getting sent to the ValidatorAddr
         -The ASA must have:
           - Total = 1
           - UnitName=VLDITR
           - GnfAdminAddr as manage
           - AssetName and
           - Url not blank.
        - The transfer amount must be 1
        [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html#tavalidator-certificate)
        """
        raise NotImplementedError("Implement check for axiom 2")

    @root_validator
    def check_axiom_3(cls, v: dict) -> dict:
        """
        Axiom 3: TaValidator has opted in.
        ValidatorAddr must be opted into the transferring ASA.
        """
        raise NotImplementedError("Implement check for axiom 3")

    @root_validator
    def check_axiom_5(cls, v: dict) -> dict:
        """
        Axiom 5: TaValidator has signed.
        ValidatorAddr must have signed the mtx.
        """
        raise NotImplementedError("Implement check for axiom 5")

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class TavalidatorcertAlgoTransfer_Maker:
    type_name = "tavalidatorcert.algo.transfer"
    version = "000"

    def __init__(self, validator_addr: str, half_signed_cert_transfer_mtx: str):
        self.tuple = TavalidatorcertAlgoTransfer(
            ValidatorAddr=validator_addr,
            HalfSignedCertTransferMtx=half_signed_cert_transfer_mtx,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: TavalidatorcertAlgoTransfer) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> TavalidatorcertAlgoTransfer:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> TavalidatorcertAlgoTransfer:
        d2 = dict(d)
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "HalfSignedCertTransferMtx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HalfSignedCertTransferMtx")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return TavalidatorcertAlgoTransfer(
            ValidatorAddr=d2["ValidatorAddr"],
            HalfSignedCertTransferMtx=d2["HalfSignedCertTransferMtx"],
            TypeName=d2["TypeName"],
            Version="000",
        )
