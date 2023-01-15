"""Type g.node.gt, version 002"""
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

from gridworks.data_classes.g_node import GNode
from gridworks.enums import GNodeRole
from gridworks.enums import GNodeStatus
from gridworks.errors import SchemaError
from gridworks.message import as_enum


class GNodeRole000SchemaEnum:
    enum_name: str = "g.node.role.000"
    symbols: List[str] = [
        "00000000",
        "bdeaa0b1",
        "8021dcad",
        "304890c5",
        "8eb5b9e1",
        "234cfaa2",
        "fec0c127",
        "3901c7d2",
        "c499943c",
        "88112a93",
        "674ad859",
        "2161739f",
        "1dce1efd",
        "db57d184",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class GNodeRole000(StrEnum):
    GNode = auto()
    TerminalAsset = auto()
    AtomicTNode = auto()
    MarketMaker = auto()
    AtomicMeteringNode = auto()
    ConductorTopologyNode = auto()
    InterconnectionComponent = auto()
    World = auto()
    TimeCoordinator = auto()
    Supervisor = auto()
    Scada = auto()
    PriceService = auto()
    WeatherService = auto()
    AggregatedTNode = auto()

    @classmethod
    def default(cls) -> "GNodeRole000":
        return cls.GNode

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class GNodeRoleMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> GNodeRole:
        if not GNodeRole000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to GNodeRole000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, GNodeRole, GNodeRole.default())

    @classmethod
    def local_to_type(cls, g_node_role: GNodeRole) -> str:
        if not isinstance(g_node_role, GNodeRole):
            raise SchemaError(f"{g_node_role} must be of type {GNodeRole}")
        versioned_enum = as_enum(g_node_role, GNodeRole000, GNodeRole000.default())
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, GNodeRole000] = {
        "00000000": GNodeRole000.GNode,
        "bdeaa0b1": GNodeRole000.TerminalAsset,
        "8021dcad": GNodeRole000.AtomicTNode,
        "304890c5": GNodeRole000.MarketMaker,
        "8eb5b9e1": GNodeRole000.AtomicMeteringNode,
        "234cfaa2": GNodeRole000.ConductorTopologyNode,
        "fec0c127": GNodeRole000.InterconnectionComponent,
        "3901c7d2": GNodeRole000.World,
        "c499943c": GNodeRole000.TimeCoordinator,
        "88112a93": GNodeRole000.Supervisor,
        "674ad859": GNodeRole000.Scada,
        "2161739f": GNodeRole000.PriceService,
        "1dce1efd": GNodeRole000.WeatherService,
        "db57d184": GNodeRole000.AggregatedTNode,
    }

    versioned_enum_to_type_dict: Dict[GNodeRole000, str] = {
        GNodeRole000.GNode: "00000000",
        GNodeRole000.TerminalAsset: "bdeaa0b1",
        GNodeRole000.AtomicTNode: "8021dcad",
        GNodeRole000.MarketMaker: "304890c5",
        GNodeRole000.AtomicMeteringNode: "8eb5b9e1",
        GNodeRole000.ConductorTopologyNode: "234cfaa2",
        GNodeRole000.InterconnectionComponent: "fec0c127",
        GNodeRole000.World: "3901c7d2",
        GNodeRole000.TimeCoordinator: "c499943c",
        GNodeRole000.Supervisor: "88112a93",
        GNodeRole000.Scada: "674ad859",
        GNodeRole000.PriceService: "2161739f",
        GNodeRole000.WeatherService: "1dce1efd",
        GNodeRole000.AggregatedTNode: "db57d184",
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


class GNodeGt(BaseModel):
    """Used to send and receive updates about GNodes.

    GNodes are the building blocks of Gridworks. They have slowly-changing state
    that must be kept in sync across a distributed system. Therefore, they require
    a global registry to act as Single Source of Truth (SSoT). This class is used for
    that SSoT to share information with actors about their GNodes, and the GNodes
    that they will observe and communicate with.
    [More info](https://gridworks.readthedocs.io/en/latest/g-node.html).
    """

    GNodeId: str = Field(
        title="Immutable identifier for GNode",
    )
    Alias: str = Field(
        title="Structured mutable identifier for GNode",
        description="The GNode Aliases are used for organizing how actors in Gridworks communicate. Together, they also encode the known topology of the electric grid. [More info](https://gridworks.readthedocs.io/en/latest/g-node-alias.html).",
    )
    Status: GNodeStatus = Field(
        title="Lifecycle indicator",
    )
    Role: GNodeRole = Field(
        title="Role within Gridworks",
        description=" [More info](https://gridworks.readthedocs.io/en/latest/g-node-role.html).",
    )
    GNodeRegistryAddr: str = Field(
        title="Algorand address for GNodeRegistry",
        description="For actors in a Gridworks world, the GNodeRegistry is the Single Source of Truth for existence and updates to GNodes. [More info](https://gridworks.readthedocs.io/en/latest/g-node-registry.html).",
    )
    PrevAlias: Optional[str] = Field(
        title="Previous GNodeAlias",
        description="As the topology of the grid updates, GNodeAliases will change to reflect that. This may happen a handful of times over the life of a GNode.",
        default=None,
    )
    GpsPointId: Optional[str] = Field(
        title="Lat/lon of GNode",
        description="Some GNodes, in particular those acting as avatars for physical devices that are part of or are attached to the electric grid, have physical locations. These locations are used to help validate the grid topology.",
        default=None,
    )
    OwnershipDeedId: Optional[int] = Field(
        title="Algorand Id of ASA Deed",
        description="The Id of the TaDeed Algorand Standard Asset if the GNode is a TerminalAsset. [More info](https://gridworks.readthedocs.io/en/latest/ta-deed.html).",
        default=None,
    )
    OwnershipDeedValidatorAddr: Optional[str] = Field(
        title="Algorand address of Validator",
        description="Deeds are issued by the GNodeFactory, in partnership with third party Validators. [More info](https://gridworks.readthedocs.io/en/latest/ta-validator.html).",
        default=None,
    )
    OwnerAddr: Optional[str] = Field(
        title="Algorand address of the deed owner",
        default=None,
    )
    DaemonAddr: Optional[str] = Field(
        title="Algorand address of the daemon app",
        description="Some GNodes have Daemon applications associated to them to handle blockchain operations.",
        default=None,
    )
    TradingRightsId: Optional[int] = Field(
        title="Algorand Id of ASA TradingRights",
        description="The Id of the TradingRights Algorand Standard Asset.",
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
    ComponentId: Optional[str] = Field(
        title="Unique identifier for GNode's Component",
        description="Used if a GNode is an avatar for a physical device. The serial number of a device is different from its make/model. The ComponentId captures the specific instance of the device.",
        default=None,
    )
    DisplayName: Optional[str] = Field(
        title="Display Name",
        default=None,
    )
    TypeName: Literal["g.node.gt"] = "g.node.gt"
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
    def _check_role(cls, v: GNodeRole) -> GNodeRole:
        return as_enum(v, GNodeRole, GNodeRole.GNode)

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

    @validator("ComponentId")
    def _check_component_id(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"ComponentId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["Status"]
        Status = as_enum(self.Status, GNodeStatus, GNodeStatus.default())
        d["StatusGtEnumSymbol"] = GNodeStatusMap.local_to_type(Status)
        del d["Role"]
        Role = as_enum(self.Role, GNodeRole, GNodeRole.default())
        d["RoleGtEnumSymbol"] = GNodeRoleMap.local_to_type(Role)
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
        if d["ComponentId"] is None:
            del d["ComponentId"]
        if d["DisplayName"] is None:
            del d["DisplayName"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class GNodeGt_Maker:
    type_name = "g.node.gt"
    version = "002"

    def __init__(
        self,
        g_node_id: str,
        alias: str,
        status: GNodeStatus,
        role: GNodeRole,
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
        component_id: Optional[str],
        display_name: Optional[str],
    ):
        self.tuple = GNodeGt(
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
            ComponentId=component_id,
            DisplayName=display_name,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GNodeGt) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GNodeGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> GNodeGt:
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
        if d2["RoleGtEnumSymbol"] in GNodeRole000SchemaEnum.symbols:
            d2["Role"] = GNodeRoleMap.type_to_local(d2["RoleGtEnumSymbol"])
        else:
            d2["Role"] = GNodeRole.default()
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
        if "ComponentId" not in d2.keys():
            d2["ComponentId"] = None
        if "DisplayName" not in d2.keys():
            d2["DisplayName"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return GNodeGt(
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
            ComponentId=d2["ComponentId"],
            DisplayName=d2["DisplayName"],
            TypeName=d2["TypeName"],
            Version="002",
        )

    @classmethod
    def tuple_to_dc(cls, t: GNodeGt) -> GNode:
        if t.GNodeId in GNode.by_id.keys():
            dc = GNode.by_id[t.GNodeId]
        else:
            dc = GNode(
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
                component_id=t.ComponentId,
                display_name=t.DisplayName,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: GNode) -> GNodeGt:
        t = GNodeGt_Maker(
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
            component_id=dc.component_id,
            display_name=dc.display_name,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> GNode:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: GNode) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> GNode:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
