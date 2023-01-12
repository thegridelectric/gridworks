"""Type sim.timestep, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gridworks.errors import SchemaError


def check_is_reasonable_unix_time_s(v: int) -> None:
    """
    ReasonableUnixTimeS format: time in unix seconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeS format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp > v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp < v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be before Jan 1 3000")


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


def check_is_reasonable_unix_time_ms(v: str) -> None:
    """
    ReasonableUnixTimeMs format: time in unix milliseconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeMs format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be before Jan 1 3000")


class SimTimestep(BaseModel):
    """Sent by TimeCoordinators to coordinate time.

    For simulated actors, time progresses discretely on receipt of these time steps.
    """

    FromGNodeAlias: str = Field(
        title="The GNodeAlias of the sender",
        description="The sender should always be a GNode Actor of role TimeCoordinator.",
    )
    FromGNodeInstanceId: str = Field(
        title="The GNodeInstanceId of the sender",
    )
    TimeUnixS: int = Field(
        title="Current time in unix seconds",
    )
    TimestepCreatedMs: int = Field(
        title="The real time created, in unix milliseconds",
    )
    MessageId: str = Field(
        title="MessageId",
    )
    TypeName: Literal["sim.timestep"] = "sim.timestep"
    Version: str = "000"

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

    @validator("TimeUnixS")
    def _check_time_unix_s(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_s(v)
        except ValueError as e:
            raise ValueError(
                f"TimeUnixS failed ReasonableUnixTimeS format validation: {e}"
            )
        return v

    @validator("TimestepCreatedMs")
    def _check_timestep_created_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"TimestepCreatedMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    @validator("MessageId")
    def _check_message_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"MessageId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

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
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SimTimestep:
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
