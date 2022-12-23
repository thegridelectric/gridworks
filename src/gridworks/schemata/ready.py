"""Type ready, version 001"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gridworks.property_format as property_format
from gridworks.errors import SchemaError
from gridworks.property_format import predicate_validator


class Ready(BaseModel):
    TimeUnixS: int  #
    FromGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    TypeName: Literal["ready"] = "ready"
    Version: str = "001"

    _validator_from_g_node_alias = predicate_validator(
        "FromGNodeAlias", property_format.is_lrd_alias_format
    )

    _validator_from_g_node_instance_id = predicate_validator(
        "FromGNodeInstanceId", property_format.is_uuid_canonical_textual
    )

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class Ready_Maker:
    type_name = "ready"
    version = "001"

    def __init__(
        self, time_unix_s: int, from_g_node_alias: str, from_g_node_instance_id: str
    ):
        self.tuple = Ready(
            TimeUnixS=time_unix_s,
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: Ready) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> Ready:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> Ready:
        d2 = dict(d)
        if "TimeUnixS" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TimeUnixS")
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return Ready(
            TimeUnixS=d2["TimeUnixS"],
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            TypeName=d2["TypeName"],
            Version="001",
        )
