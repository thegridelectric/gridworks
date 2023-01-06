"""Type heartbeat.a, version 100"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gridworks.errors import SchemaError


def check_is_hex_char(v: str) -> None:
    """HexChar format: single-char string in '0123456789abcdefABCDEF'

    Raises:
        ValueError: if v is not HexChar format
    """
    if not isinstance(v, str):
        raise ValueError(f"{v} must be a hex char, but not even a string")
    if len(v) > 1:
        raise ValueError(f"{v} must be a hex char, but not of len 1")
    if v not in "0123456789abcdefABCDEF":
        raise ValueError(f"{v} must be one of '0123456789abcdefABCDEF'")


class HeartbeatA(BaseModel):
    """Used to check that an actor can both send and receive messages.

    For use between two actors sending direct messages to each other,
    for example a Supervisor and one of its subordinates.

    `More info <https://gridworks.readthedocs.io/en/latest/g-node-instance.html>`_

    """

    MyHex: str = Field(
        title="Hex character getting sent",
        description="HexChar format",
    )
    YourLastHex: str = Field(
        title="Last hex character received from heartbeat partner",
        description="HexChar format",
    )  #
    TypeName: Literal["heartbeat.a"] = "heartbeat.a"
    Version: str = "100"

    @validator("MyHex")
    def _validator_my_hex(cls, v: str) -> str:
        try:
            check_is_hex_char(v)
        except ValueError as e:
            raise ValueError(f"MyHex failed HexChar format validation: {e}")
        return v

    @validator("YourLastHex")
    def _validator_your_last_hex(cls, v: str) -> str:
        try:
            check_is_hex_char(v)
        except ValueError as e:
            raise ValueError(f"YourLastHex failed HexChar format validation: {e}")
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        """
        Returns:
            str: corresponding serialized json string of type ```heartbeat.a```
        """
        return json.dumps(self.as_dict())


class HeartbeatA_Maker:
    """Helper for translating between json ```heartbeat.a``` types
    and python ```HeartbeatA``` tuples.
    """

    type_name = "heartbeat.a"
    version = "100"

    def __init__(self, my_hex: str, your_last_hex: str):
        self.tuple = HeartbeatA(
            MyHex=my_hex,
            YourLastHex=your_last_hex,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: HeartbeatA) -> str:
        """
        Args:
             tuple (HeartbeatA)

        Returns:
            str:  corresponding serialized json string of type ```heartbeat.a```
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> HeartbeatA:
        """
        Args:
            t (str): Serialized json string of type ```heartbeat.a```

        Returns:
            HeartbeatA: corresponding HeartbeatA object
        """
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
            Version="100",
        )
