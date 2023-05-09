"""Type base.g.node.gt, version 002"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from fastapi_utils.enums import StrEnum
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gridworks.data_classes.base_g_node import BaseGNode
from gridworks.enums import CoreGNodeRole
from gridworks.enums import GNodeStatus
from gridworks.errors import SchemaError
from gridworks.message import as_enum


class CoreGNodeRole000SchemaEnum:
    enum_name: str = "core.g.node.role.000"
    symbols: List[str] = [
        "00000000",
        "0f8872f7",
        "d9823442",
        "86f21dd2",
        "9521af06",
        "4502e355",
        "d67e564e",
        "7a8e4046",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class CoreGNodeRole000(StrEnum):
    Other = auto()
    TerminalAsset = auto()
    AtomicTNode = auto()
    MarketMaker = auto()
    AtomicMeteringNode = auto()
    ConductorTopologyNode = auto()
    InterconnectionComponent = auto()
    Scada = auto()

    @classmethod
    def default(cls) -> "CoreGNodeRole000":
        return cls.Other

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class CoreGNodeRoleMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> CoreGNodeRole:
        if not CoreGNodeRole000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to CoreGNodeRole000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, CoreGNodeRole, CoreGNodeRole.default())

    @classmethod
    def local_to_type(cls, core_g_node_role: CoreGNodeRole) -> str:
        if not isinstance(core_g_node_role, CoreGNodeRole):
            raise SchemaError(f"{core_g_node_role} must be of type {CoreGNodeRole}")
        versioned_enum = as_enum(
            core_g_node_role, CoreGNodeRole000, CoreGNodeRole000.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, CoreGNodeRole000] = {
        "00000000": CoreGNodeRole000.Other,
        "0f8872f7": CoreGNodeRole000.TerminalAsset,
        "d9823442": CoreGNodeRole000.AtomicTNode,
        "86f21dd2": CoreGNodeRole000.MarketMaker,
        "9521af06": CoreGNodeRole000.AtomicMeteringNode,
        "4502e355": CoreGNodeRole000.ConductorTopologyNode,
        "d67e564e": CoreGNodeRole000.InterconnectionComponent,
        "7a8e4046": CoreGNodeRole000.Scada,
    }

    versioned_enum_to_type_dict: Dict[CoreGNodeRole000, str] = {
        CoreGNodeRole000.Other: "00000000",
        CoreGNodeRole000.TerminalAsset: "0f8872f7",
        CoreGNodeRole000.AtomicTNode: "d9823442",
        CoreGNodeRole000.MarketMaker: "86f21dd2",
        CoreGNodeRole000.AtomicMeteringNode: "9521af06",
        CoreGNodeRole000.ConductorTopologyNode: "4502e355",
        CoreGNodeRole000.InterconnectionComponent: "d67e564e",
        CoreGNodeRole000.Scada: "7a8e4046",
    }


class GNodeStatus100SchemaEnum:
    enum_name: str = "g.node.status.100"
    symbols: List[str] = [
        "00000000",
        "153d3475",
        "a2cfc2f7",
        "839b38db",
        "f5831e1d",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class GNodeStatus100(StrEnum):
    Unknown = auto()
    Pending = auto()
    Active = auto()
    PermanentlyDeactivated = auto()
    Suspended = auto()

    @classmethod
    def default(cls) -> "GNodeStatus100":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class GNodeStatusMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> GNodeStatus:
        if not GNodeStatus100SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to GNodeStatus100 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, GNodeStatus, GNodeStatus.default())

    @classmethod
    def local_to_type(cls, g_node_status: GNodeStatus) -> str:
        if not isinstance(g_node_status, GNodeStatus):
            raise SchemaError(f"{g_node_status} must be of type {GNodeStatus}")
        versioned_enum = as_enum(
            g_node_status, GNodeStatus100, GNodeStatus100.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, GNodeStatus100] = {
        "00000000": GNodeStatus100.Unknown,
        "153d3475": GNodeStatus100.Pending,
        "a2cfc2f7": GNodeStatus100.Active,
        "839b38db": GNodeStatus100.PermanentlyDeactivated,
        "f5831e1d": GNodeStatus100.Suspended,
    }

    versioned_enum_to_type_dict: Dict[GNodeStatus100, str] = {
        GNodeStatus100.Unknown: "00000000",
        GNodeStatus100.Pending: "153d3475",
        GNodeStatus100.Active: "a2cfc2f7",
        GNodeStatus100.PermanentlyDeactivated: "839b38db",
        GNodeStatus100.Suspended: "f5831e1d",
    }


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


def check_is_algo_address_string_format(v: str) -> None:
    """
    AlgoAddressStringFormat format: The public key of a private/public Ed25519
    key pair, transformed into an  Algorand address, by adding a 4-byte checksum
    to the end of the public key and then encoding in base32.

    Raises:
        ValueError: if not AlgoAddressStringFormat format
    """
    import algosdk

    at = algosdk.abi.AddressType()
    try:
        result = at.decode(at.encode(v))
    except Exception as e:
        raise ValueError(f"Not AlgoAddressStringFormat: {e}")


class BaseGNodeGt(BaseModel):
    """.

    BaseGNode. Authority is GNodeFactory.
    """

    GNodeId: str = Field(
        title="GNodeId",
    )
    Alias: str = Field(
        title="Alias",
    )
    Status: GNodeStatus = Field(
        title="Status",
    )
    Role: CoreGNodeRole = Field(
        title="Role",
    )
    GNodeRegistryAddr: str = Field(
        title="GNodeRegistryAddr",
    )
    PrevAlias: Optional[str] = Field(
        title="PrevAlias",
        default=None,
    )
    GpsPointId: Optional[str] = Field(
        title="GpsPointId",
        default=None,
    )
    OwnershipDeedId: Optional[int] = Field(
        title="OwnershipDeedId",
        default=None,
    )
    OwnershipDeedValidatorAddr: Optional[str] = Field(
        title="OwnershipDeedValidatorAddr",
        default=None,
    )
    OwnerAddr: Optional[str] = Field(
        title="OwnerAddr",
        default=None,
    )
    DaemonAddr: Optional[str] = Field(
        title="DaemonAddr",
        default=None,
    )
    TradingRightsId: Optional[int] = Field(
        title="TradingRightsId",
        default=None,
    )
    ScadaAlgoAddr: Optional[str] = Field(
        title="ScadaAlgoAddr",
        default=None,
    )
    ScadaCertId: Optional[int] = Field(
        title="ScadaCertId",
        default=None,
    )
    TypeName: Literal["base.g.node.gt"] = "base.g.node.gt"
    Version: str = "002"

    @validator("GNodeId")
    def _check_g_node_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"GNodeId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("Alias")
    def _check_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"Alias failed LeftRightDot format validation: {e}")
        return v

    @validator("Status")
    def _check_status(cls, v: GNodeStatus) -> GNodeStatus:
        return as_enum(v, GNodeStatus, GNodeStatus.Unknown)

    @validator("Role")
    def _check_role(cls, v: CoreGNodeRole) -> CoreGNodeRole:
        return as_enum(v, CoreGNodeRole, CoreGNodeRole.Other)

    @validator("GNodeRegistryAddr")
    def _check_g_node_registry_addr(cls, v: str) -> str:
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"GNodeRegistryAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("PrevAlias")
    def _check_prev_alias(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"PrevAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("GpsPointId")
    def _check_gps_point_id(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"GpsPointId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("OwnershipDeedValidatorAddr")
    def _check_ownership_deed_validator_addr(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"OwnershipDeedValidatorAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("OwnerAddr")
    def _check_owner_addr(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"OwnerAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("DaemonAddr")
    def _check_daemon_addr(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"DaemonAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    @validator("ScadaAlgoAddr")
    def _check_scada_algo_addr(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"ScadaAlgoAddr failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["Status"]
        Status = as_enum(self.Status, GNodeStatus, GNodeStatus.default())
        d["StatusGtEnumSymbol"] = GNodeStatusMap.local_to_type(Status)
        del d["Role"]
        Role = as_enum(self.Role, CoreGNodeRole, CoreGNodeRole.default())
        d["RoleGtEnumSymbol"] = CoreGNodeRoleMap.local_to_type(Role)
        if d["PrevAlias"] is None:
            del d["PrevAlias"]
        if d["GpsPointId"] is None:
            del d["GpsPointId"]
        if d["OwnershipDeedId"] is None:
            del d["OwnershipDeedId"]
        if d["OwnershipDeedValidatorAddr"] is None:
            del d["OwnershipDeedValidatorAddr"]
        if d["OwnerAddr"] is None:
            del d["OwnerAddr"]
        if d["DaemonAddr"] is None:
            del d["DaemonAddr"]
        if d["TradingRightsId"] is None:
            del d["TradingRightsId"]
        if d["ScadaAlgoAddr"] is None:
            del d["ScadaAlgoAddr"]
        if d["ScadaCertId"] is None:
            del d["ScadaCertId"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class BaseGNodeGt_Maker:
    type_name = "base.g.node.gt"
    version = "002"

    def __init__(
        self,
        g_node_id: str,
        alias: str,
        status: GNodeStatus,
        role: CoreGNodeRole,
        g_node_registry_addr: str,
        prev_alias: Optional[str],
        gps_point_id: Optional[str],
        ownership_deed_id: Optional[int],
        ownership_deed_validator_addr: Optional[str],
        owner_addr: Optional[str],
        daemon_addr: Optional[str],
        trading_rights_id: Optional[int],
        scada_algo_addr: Optional[str],
        scada_cert_id: Optional[int],
    ):
        self.tuple = BaseGNodeGt(
            GNodeId=g_node_id,
            Alias=alias,
            Status=status,
            Role=role,
            GNodeRegistryAddr=g_node_registry_addr,
            PrevAlias=prev_alias,
            GpsPointId=gps_point_id,
            OwnershipDeedId=ownership_deed_id,
            OwnershipDeedValidatorAddr=ownership_deed_validator_addr,
            OwnerAddr=owner_addr,
            DaemonAddr=daemon_addr,
            TradingRightsId=trading_rights_id,
            ScadaAlgoAddr=scada_algo_addr,
            ScadaCertId=scada_cert_id,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: BaseGNodeGt) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> BaseGNodeGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> BaseGNodeGt:
        d2 = dict(d)
        if "GNodeId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeId")
        if "Alias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Alias")
        if "StatusGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StatusGtEnumSymbol")
        if d2["StatusGtEnumSymbol"] in GNodeStatus100SchemaEnum.symbols:
            d2["Status"] = GNodeStatusMap.type_to_local(d2["StatusGtEnumSymbol"])
        else:
            d2["Status"] = GNodeStatus.default()
        if "RoleGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing RoleGtEnumSymbol")
        if d2["RoleGtEnumSymbol"] in CoreGNodeRole000SchemaEnum.symbols:
            d2["Role"] = CoreGNodeRoleMap.type_to_local(d2["RoleGtEnumSymbol"])
        else:
            d2["Role"] = CoreGNodeRole.default()
        if "GNodeRegistryAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeRegistryAddr")
        if "PrevAlias" not in d2.keys():
            d2["PrevAlias"] = None
        if "GpsPointId" not in d2.keys():
            d2["GpsPointId"] = None
        if "OwnershipDeedId" not in d2.keys():
            d2["OwnershipDeedId"] = None
        if "OwnershipDeedValidatorAddr" not in d2.keys():
            d2["OwnershipDeedValidatorAddr"] = None
        if "OwnerAddr" not in d2.keys():
            d2["OwnerAddr"] = None
        if "DaemonAddr" not in d2.keys():
            d2["DaemonAddr"] = None
        if "TradingRightsId" not in d2.keys():
            d2["TradingRightsId"] = None
        if "ScadaAlgoAddr" not in d2.keys():
            d2["ScadaAlgoAddr"] = None
        if "ScadaCertId" not in d2.keys():
            d2["ScadaCertId"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return BaseGNodeGt(
            GNodeId=d2["GNodeId"],
            Alias=d2["Alias"],
            Status=d2["Status"],
            Role=d2["Role"],
            GNodeRegistryAddr=d2["GNodeRegistryAddr"],
            PrevAlias=d2["PrevAlias"],
            GpsPointId=d2["GpsPointId"],
            OwnershipDeedId=d2["OwnershipDeedId"],
            OwnershipDeedValidatorAddr=d2["OwnershipDeedValidatorAddr"],
            OwnerAddr=d2["OwnerAddr"],
            DaemonAddr=d2["DaemonAddr"],
            TradingRightsId=d2["TradingRightsId"],
            ScadaAlgoAddr=d2["ScadaAlgoAddr"],
            ScadaCertId=d2["ScadaCertId"],
            TypeName=d2["TypeName"],
            Version="002",
        )

    @classmethod
    def tuple_to_dc(cls, t: BaseGNodeGt) -> BaseGNode:
        if t.GNodeId in BaseGNode.by_id.keys():
            dc = BaseGNode.by_id[t.GNodeId]
        else:
            dc = BaseGNode(
                g_node_id=t.GNodeId,
                alias=t.Alias,
                status=t.Status,
                role=t.Role,
                g_node_registry_addr=t.GNodeRegistryAddr,
                prev_alias=t.PrevAlias,
                gps_point_id=t.GpsPointId,
                ownership_deed_id=t.OwnershipDeedId,
                ownership_deed_validator_addr=t.OwnershipDeedValidatorAddr,
                owner_addr=t.OwnerAddr,
                daemon_addr=t.DaemonAddr,
                trading_rights_id=t.TradingRightsId,
                scada_algo_addr=t.ScadaAlgoAddr,
                scada_cert_id=t.ScadaCertId,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: BaseGNode) -> BaseGNodeGt:
        t = BaseGNodeGt_Maker(
            g_node_id=dc.g_node_id,
            alias=dc.alias,
            status=dc.status,
            role=dc.role,
            g_node_registry_addr=dc.g_node_registry_addr,
            prev_alias=dc.prev_alias,
            gps_point_id=dc.gps_point_id,
            ownership_deed_id=dc.ownership_deed_id,
            ownership_deed_validator_addr=dc.ownership_deed_validator_addr,
            owner_addr=dc.owner_addr,
            daemon_addr=dc.daemon_addr,
            trading_rights_id=dc.trading_rights_id,
            scada_algo_addr=dc.scada_algo_addr,
            scada_cert_id=dc.scada_cert_id,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> BaseGNode:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: BaseGNode) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> BaseGNode:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
