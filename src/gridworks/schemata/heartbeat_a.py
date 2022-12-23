"""Type heartbeat.a, version 001"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

from gridworks.errors import SchemaError


class HeartbeatA(BaseModel):
    MyHex: str  #
    YourLastHex: str  #
    TypeName: Literal["heartbeat.a"] = "heartbeat.a"
    Version: str = "001"

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class HeartbeatA_Maker:
    type_name = "heartbeat.a"
    version = "001"

    def __init__(self, my_hex: str, your_last_hex: str):
        self.tuple = HeartbeatA(
            MyHex=my_hex,
            YourLastHex=your_last_hex,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: HeartbeatA) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> HeartbeatA:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> HeartbeatA:
        d2 = dict(d)
        if "MyHex" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MyHex")
        if "YourLastHex" not in d2.keys():
            raise SchemaError(f"dict {d2} missing YourLastHex")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return HeartbeatA(
            MyHex=d2["MyHex"],
            YourLastHex=d2["YourLastHex"],
            TypeName=d2["TypeName"],
            Version="001",
        )
