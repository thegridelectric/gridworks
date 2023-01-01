"""Type tavalidatorcert.algo.transfer, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gridworks.property_format as property_format
from gridworks.errors import SchemaError
from gridworks.property_format import predicate_validator


class TavalidatorcertAlgoTransfer(BaseModel):
    ValidatorAddr: str  #
    HalfSignedCertTransferMtx: str  #
    TypeName: Literal["tavalidatorcert.algo.transfer"] = "tavalidatorcert.algo.transfer"
    Version: str = "000"

    _validator_validator_addr = predicate_validator(
        "ValidatorAddr", property_format.is_algo_address_string_format
    )

    _validator_half_signed_cert_transfer_mtx = predicate_validator(
        "HalfSignedCertTransferMtx", property_format.is_algo_msg_pack_encoded
    )

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
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> TavalidatorcertAlgoTransfer:
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
