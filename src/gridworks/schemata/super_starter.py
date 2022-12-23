"""Type super.starter, version 000"""
import json
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import validator

import gridworks.property_format as property_format
from gridworks.errors import SchemaError
from gridworks.schemata.g_node_instance_gt import GNodeInstanceGt
from gridworks.schemata.g_node_instance_gt import GNodeInstanceGt_Maker
from gridworks.schemata.supervisor_container_gt import SupervisorContainerGt
from gridworks.schemata.supervisor_container_gt import SupervisorContainerGt_Maker


class SuperStarter(BaseModel):
    SupervisorContainer: SupervisorContainerGt  #
    GniList: List[GNodeInstanceGt]  #
    AliasWithKeyList: List[str]  #
    KeyList: List[str]  #
    TypeName: Literal["super.starter"] = "super.starter"
    Version: str = "000"

    @validator("GniList")
    def _validator_gni_list(cls, v: List[GNodeInstanceGt]) -> List[GNodeInstanceGt]:
        for elt in v:
            if not isinstance(elt, GNodeInstanceGt):
                raise ValueError(
                    f"elt {elt} of GniList must have type GNodeInstanceGt."
                )
        return v

    @validator("AliasWithKeyList")
    def _validator_alias_with_key_list(cls, v: List[str]) -> List[str]:
        for elt in v:
            if not property_format.is_lrd_alias_format(elt):
                raise ValueError(
                    f"failure of predicate is_lrd_alias_format() on elt {elt} of AliasWithKeyList"
                )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["SupervisorContainer"] = self.SupervisorContainer.as_dict()

        # Recursively call as_dict() for the SubTypes
        gni_list = []
        for elt in self.GniList:
            gni_list.append(elt.as_dict())
        d["GniList"] = gni_list
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class SuperStarter_Maker:
    type_name = "super.starter"
    version = "000"

    def __init__(
        self,
        supervisor_container: SupervisorContainerGt,
        gni_list: List[GNodeInstanceGt],
        alias_with_key_list: List[str],
        key_list: List[str],
    ):
        self.tuple = SuperStarter(
            SupervisorContainer=supervisor_container,
            GniList=gni_list,
            AliasWithKeyList=alias_with_key_list,
            KeyList=key_list,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: SuperStarter) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SuperStarter:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> SuperStarter:
        d2 = dict(d)
        if "SupervisorContainer" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SupervisorContainer")
        if not isinstance(d2["SupervisorContainer"], dict):
            raise SchemaError(
                f"d['SupervisorContainer'] {d2['SupervisorContainer']} must be a SupervisorContainerGt!"
            )
        supervisor_container = SupervisorContainerGt_Maker.dict_to_tuple(
            d2["SupervisorContainer"]
        )
        d2["SupervisorContainer"] = supervisor_container
        if "GniList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GniList")
        gni_list = []
        if not isinstance(d2["GniList"], List):
            raise SchemaError("GniList must be a List!")
        for elt in d2["GniList"]:
            if not isinstance(elt, dict):
                raise SchemaError(
                    f"elt {elt} of GniList must be "
                    "GNodeInstanceGt but not even a dict!"
                )
            gni_list.append(GNodeInstanceGt_Maker.dict_to_tuple(elt))
        d2["GniList"] = gni_list
        if "AliasWithKeyList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AliasWithKeyList")
        if "KeyList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing KeyList")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return SuperStarter(
            SupervisorContainer=d2["SupervisorContainer"],
            GniList=d2["GniList"],
            AliasWithKeyList=d2["AliasWithKeyList"],
            KeyList=d2["KeyList"],
            TypeName=d2["TypeName"],
            Version="000",
        )
