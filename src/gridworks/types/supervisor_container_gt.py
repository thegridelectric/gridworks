"""Type supervisor.container.gt, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from gridworks.enums import GwStrEnum
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gridworks.enums import SupervisorContainerStatus
from gridworks.errors import SchemaError
from gridworks.message import as_enum


class SupervisorContainerStatus000SchemaEnum:
    enum_name: str = "supervisor.container.status.000"
    symbols: List[str] = [
        "00000000",
        "f48cff43",
        "17c5cc54",
        "ec342324",
        "cfde1b40",
        "4e28b6ae",
        "da2dafe0",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class SupervisorContainerStatus000(GwStrEnum):
    Unknown = auto()
    Authorized = auto()
    Launching = auto()
    Provisioning = auto()
    Running = auto()
    Stopped = auto()
    Deleted = auto()

    @classmethod
    def default(cls) -> "SupervisorContainerStatus000":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class SupervisorContainerStatusMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> SupervisorContainerStatus:
        if not SupervisorContainerStatus000SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to SupervisorContainerStatus000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(
            versioned_enum,
            SupervisorContainerStatus,
            SupervisorContainerStatus.default(),
        )

    @classmethod
    def local_to_type(
        cls, supervisor_container_status: SupervisorContainerStatus
    ) -> str:
        if not isinstance(supervisor_container_status, SupervisorContainerStatus):
            raise SchemaError(
                f"{supervisor_container_status} must be of type {SupervisorContainerStatus}"
            )
        versioned_enum = as_enum(
            supervisor_container_status,
            SupervisorContainerStatus000,
            SupervisorContainerStatus000.default(),
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, SupervisorContainerStatus000] = {
        "00000000": SupervisorContainerStatus000.Unknown,
        "f48cff43": SupervisorContainerStatus000.Authorized,
        "17c5cc54": SupervisorContainerStatus000.Launching,
        "ec342324": SupervisorContainerStatus000.Provisioning,
        "cfde1b40": SupervisorContainerStatus000.Running,
        "4e28b6ae": SupervisorContainerStatus000.Stopped,
        "da2dafe0": SupervisorContainerStatus000.Deleted,
    }

    versioned_enum_to_type_dict: Dict[SupervisorContainerStatus000, str] = {
        SupervisorContainerStatus000.Unknown: "00000000",
        SupervisorContainerStatus000.Authorized: "f48cff43",
        SupervisorContainerStatus000.Launching: "17c5cc54",
        SupervisorContainerStatus000.Provisioning: "ec342324",
        SupervisorContainerStatus000.Running: "cfde1b40",
        SupervisorContainerStatus000.Stopped: "4e28b6ae",
        SupervisorContainerStatus000.Deleted: "da2dafe0",
    }


def check_is_world_instance_name_format(v: str) -> None:
    """
    WorldInstanceName format: A single alphanumerical word starting
    with an alphabet char (the root GNodeAlias) and an integer,
    seperated by '__'. For example 'd1__1'

    Raises:
        ValueError: if not WorldInstanceNameFormat format
    """
    try:
        words = v.split("__")
    except:
        raise ValueError(f"{v} is not split by '__'")
    if len(words) != 2:
        raise ValueError(f"{v} not 2 words separated by '__'")
    try:
        int(words[1])
    except:
        raise ValueError(f"{v} second word not an int")

    root_g_node_alias = words[0]
    first_char = root_g_node_alias[0]
    if not first_char.isalpha():
        raise ValueError(f"{v} first word must be alph char")
    if not root_g_node_alias.isalnum():
        raise ValueError(f"{v} first word must be alphanumeric")


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


class SupervisorContainerGt(BaseModel):
    """Used to send and receive updates about SupervisorContainers.

    Sent from a GNodeRegistry to a World, and used also by the World as it spawns
    GNodeInstances in docker instances (i.e., the SupervisorContainers).
    [More info](https://gridworks.readthedocs.io/en/latest/supervisor.html).
    """

    SupervisorContainerId: str = Field(
        title="Id of the docker SupervisorContainer",
    )
    Status: SupervisorContainerStatus = Field(
        title="Status",
    )
    WorldInstanceName: str = Field(
        title="Name of the WorldInstance",
        description="For example, d1__1 is a potential name for a World whose World GNode has alias d1.",
    )
    SupervisorGNodeInstanceId: str = Field(
        title="Id of the SupervisorContainer's prime actor (aka the Supervisor GNode)",
    )
    SupervisorGNodeAlias: str = Field(
        title="Alias of the SupervisorContainer's prime actor (aka the Supervisor GNode)",
    )
    TypeName: Literal["supervisor.container.gt"] = "supervisor.container.gt"
    Version: str = "000"

    @validator("SupervisorContainerId")
    def _check_supervisor_container_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"SupervisorContainerId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("Status")
    def _check_status(cls, v: SupervisorContainerStatus) -> SupervisorContainerStatus:
        return as_enum(v, SupervisorContainerStatus, SupervisorContainerStatus.Unknown)

    @validator("WorldInstanceName")
    def _check_world_instance_name(cls, v: str) -> str:
        try:
            check_is_world_instance_name_format(v)
        except ValueError as e:
            raise ValueError(
                f"WorldInstanceName failed WorldInstanceNameFormat format validation: {e}"
            )
        return v

    @validator("SupervisorGNodeInstanceId")
    def _check_supervisor_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"SupervisorGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("SupervisorGNodeAlias")
    def _check_supervisor_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"SupervisorGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["Status"]
        Status = as_enum(
            self.Status, SupervisorContainerStatus, SupervisorContainerStatus.default()
        )
        d["StatusGtEnumSymbol"] = SupervisorContainerStatusMap.local_to_type(Status)
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class SupervisorContainerGt_Maker:
    type_name = "supervisor.container.gt"
    version = "000"

    def __init__(
        self,
        supervisor_container_id: str,
        status: SupervisorContainerStatus,
        world_instance_name: str,
        supervisor_g_node_instance_id: str,
        supervisor_g_node_alias: str,
    ):
        self.tuple = SupervisorContainerGt(
            SupervisorContainerId=supervisor_container_id,
            Status=status,
            WorldInstanceName=world_instance_name,
            SupervisorGNodeInstanceId=supervisor_g_node_instance_id,
            SupervisorGNodeAlias=supervisor_g_node_alias,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: SupervisorContainerGt) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SupervisorContainerGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> SupervisorContainerGt:
        d2 = dict(d)
        if "SupervisorContainerId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SupervisorContainerId")
        if "StatusGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StatusGtEnumSymbol")
        if d2["StatusGtEnumSymbol"] in SupervisorContainerStatus000SchemaEnum.symbols:
            d2["Status"] = SupervisorContainerStatusMap.type_to_local(
                d2["StatusGtEnumSymbol"]
            )
        else:
            d2["Status"] = SupervisorContainerStatus.default()
        if "WorldInstanceName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing WorldInstanceName")
        if "SupervisorGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SupervisorGNodeInstanceId")
        if "SupervisorGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SupervisorGNodeAlias")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return SupervisorContainerGt(
            SupervisorContainerId=d2["SupervisorContainerId"],
            Status=d2["Status"],
            WorldInstanceName=d2["WorldInstanceName"],
            SupervisorGNodeInstanceId=d2["SupervisorGNodeInstanceId"],
            SupervisorGNodeAlias=d2["SupervisorGNodeAlias"],
            TypeName=d2["TypeName"],
            Version="000",
        )
