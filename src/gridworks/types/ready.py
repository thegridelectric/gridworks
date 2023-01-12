"""Type ready, version 001"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gridworks.errors import SchemaError


def check_is_uuid_canonical_textual(v: str) -> None:
    """
    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Raises:
        ValueError: if not UuidCanonicalTextual format
    """
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"{v} split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of {v} are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")


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


class Ready(BaseModel):
    """Used in simulations by TimeCoordinator GNodes.

    Only intended for simulations that do not have sub-second TimeSteps.
    TimeCoordinators based on ```gridworks-timecoordinator``` have a notion of actors
    whose `Ready` must be received before issuing the next TimeStep.
    [More info](https://gridworks.readthedocs.io/en/latest/time-coordinator.html).
    """

    FromGNodeAlias: str = Field(
        title="The GNodeAlias of the sender",
    )
    FromGNodeInstanceId: str = Field(
        title="The GNodeInstanceId of the sender",
    )
    TimeUnixS: int = Field(
        title="Latest simulated time for sender",
        description="The time in unix seconds of the latest TimeStep received from the TimeCoordinator by the actor that sent the payload.",
    )
    TypeName: Literal["ready"] = "ready"
    Version: str = "001"

    @validator("FromGNodeAlias")
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("FromGNodeInstanceId")
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class Ready_Maker:
    type_name = "ready"
    version = "001"

    def __init__(
        self, from_g_node_alias: str, from_g_node_instance_id: str, time_unix_s: int
    ):
        self.tuple = Ready(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            TimeUnixS=time_unix_s,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: Ready) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> Ready:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> Ready:
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "TimeUnixS" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TimeUnixS")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return Ready(
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            TimeUnixS=d2["TimeUnixS"],
            TypeName=d2["TypeName"],
            Version="001",
        )
