"""Type supervisor.container.gt, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from fastapi_utils.enums import StrEnum
from pydantic import BaseModel
from pydantic import validator

import gridworks.property_format as property_format
from gridworks.enums import SupervisorContainerStatus
from gridworks.errors import SchemaError
from gridworks.message import as_enum
from gridworks.property_format import predicate_validator


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


class SupervisorContainerStatus000(StrEnum):
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


class SupervisorContainerGt(BaseModel):
    SupervisorContainerId: str  #
    Status: SupervisorContainerStatus  #
    WorldInstanceAlias: str  #
    SupervisorGNodeInstanceId: str  #
    SupervisorGNodeAlias: str  #
    TypeName: Literal["supervisor.container.gt"] = "supervisor.container.gt"
    Version: str = "000"

    _validator_supervisor_container_id = predicate_validator(
        "SupervisorContainerId", property_format.is_uuid_canonical_textual
    )

    @validator("Status")
    def _validator_status(
        cls, v: SupervisorContainerStatus
    ) -> SupervisorContainerStatus:
        return as_enum(v, SupervisorContainerStatus, SupervisorContainerStatus.Unknown)

    _validator_world_instance_alias = predicate_validator(
        "WorldInstanceAlias", property_format.is_world_instance_alias_format
    )

    _validator_supervisor_g_node_instance_id = predicate_validator(
        "SupervisorGNodeInstanceId", property_format.is_uuid_canonical_textual
    )

    _validator_supervisor_g_node_alias = predicate_validator(
        "SupervisorGNodeAlias", property_format.is_lrd_alias_format
    )

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
        world_instance_alias: str,
        supervisor_g_node_instance_id: str,
        supervisor_g_node_alias: str,
    ):
        self.tuple = SupervisorContainerGt(
            SupervisorContainerId=supervisor_container_id,
            Status=status,
            WorldInstanceAlias=world_instance_alias,
            SupervisorGNodeInstanceId=supervisor_g_node_instance_id,
            SupervisorGNodeAlias=supervisor_g_node_alias,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: SupervisorContainerGt) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SupervisorContainerGt:
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
        if "WorldInstanceAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing WorldInstanceAlias")
        if "SupervisorGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SupervisorGNodeInstanceId")
        if "SupervisorGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SupervisorGNodeAlias")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return SupervisorContainerGt(
            SupervisorContainerId=d2["SupervisorContainerId"],
            Status=d2["Status"],
            WorldInstanceAlias=d2["WorldInstanceAlias"],
            SupervisorGNodeInstanceId=d2["SupervisorGNodeInstanceId"],
            SupervisorGNodeAlias=d2["SupervisorGNodeAlias"],
            TypeName=d2["TypeName"],
            Version="000",
        )
