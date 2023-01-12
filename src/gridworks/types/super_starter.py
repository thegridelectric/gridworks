"""Type super.starter, version 000"""
import json
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gridworks.errors import SchemaError
from gridworks.types.g_node_instance_gt import GNodeInstanceGt
from gridworks.types.g_node_instance_gt import GNodeInstanceGt_Maker
from gridworks.types.supervisor_container_gt import SupervisorContainerGt
from gridworks.types.supervisor_container_gt import SupervisorContainerGt_Maker


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


class SuperStarter(BaseModel):
    """Used by world to seed a docker container with data needed to spawn and superviser GNodeInstances"""

    SupervisorContainer: SupervisorContainerGt = Field(
        title="Key data about the docker container",
    )
    GniList: List[GNodeInstanceGt] = Field(
        title="List of GNodeInstances (Gnis) run in the container",
    )
    AliasWithKeyList: List[str] = Field(
        title="Aliases of Gnis that own Algorand secret keys",
    )
    KeyList: List[str] = Field(
        title="Algorand secret keys owned by Gnis",
    )
    TypeName: Literal["super.starter"] = "super.starter"
    Version: str = "000"

    @validator("GniList")
    def _check_gni_list(cls, v: List) -> List:
        for elt in v:
            if not isinstance(elt, GNodeInstanceGt):
                raise ValueError(
                    f"elt {elt} of GniList must have type GNodeInstanceGt."
                )
        return v

    @validator("AliasWithKeyList")
    def _check_alias_with_key_list(cls, v: List) -> List:
        for elt in v:
            try:
                check_is_left_right_dot(elt)
            except ValueError as e:
                raise ValueError(
                    f"AliasWithKeyList element {elt} failed LeftRightDot format validation: {e}"
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
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SuperStarter:
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
