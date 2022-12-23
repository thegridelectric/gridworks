"""Type sim.timestep, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gridworks.property_format as property_format
from gridworks.errors import SchemaError
from gridworks.property_format import predicate_validator


class SimTimestep(BaseModel):
    FromGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    TimeUnixS: int  #
    TimestepCreatedMs: int  #
    MessageId: str  #
    TypeName: Literal["sim.timestep"] = "sim.timestep"
    Version: str = "000"

    _validator_from_g_node_alias = predicate_validator(
        "FromGNodeAlias", property_format.is_lrd_alias_format
    )

    _validator_from_g_node_instance_id = predicate_validator(
        "FromGNodeInstanceId", property_format.is_uuid_canonical_textual
    )

    _validator_time_unix_s = predicate_validator(
        "TimeUnixS", property_format.is_reasonable_unix_time_s
    )

    _validator_timestep_created_ms = predicate_validator(
        "TimestepCreatedMs", property_format.is_reasonable_unix_time_ms
    )

    _validator_message_id = predicate_validator(
        "MessageId", property_format.is_uuid_canonical_textual
    )

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class SimTimestep_Maker:
    type_name = "sim.timestep"
    version = "000"

    def __init__(
        self,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        time_unix_s: int,
        timestep_created_ms: int,
        message_id: str,
    ):
        self.tuple = SimTimestep(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            TimeUnixS=time_unix_s,
            TimestepCreatedMs=timestep_created_ms,
            MessageId=message_id,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: SimTimestep) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SimTimestep:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> SimTimestep:
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "TimeUnixS" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TimeUnixS")
        if "TimestepCreatedMs" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TimestepCreatedMs")
        if "MessageId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MessageId")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return SimTimestep(
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            TimeUnixS=d2["TimeUnixS"],
            TimestepCreatedMs=d2["TimestepCreatedMs"],
            MessageId=d2["MessageId"],
            TypeName=d2["TypeName"],
            Version="000",
        )
