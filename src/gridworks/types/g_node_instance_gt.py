"""Type g.node.instance.gt, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from gridworks.enums import GwStrEnum
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from gridworks.data_classes.g_node_instance import GNodeInstance
from gridworks.enums import GniStatus
from gridworks.enums import StrategyName
from gridworks.errors import SchemaError
from gridworks.message import as_enum
from gridworks.types.g_node_gt import GNodeGt
from gridworks.types.g_node_gt import GNodeGt_Maker


class GniStatus000SchemaEnum:
    enum_name: str = "gni.status.000"
    symbols: List[str] = [
        "00000000",
        "7890ab0a",
        "69241259",
        "8222421f",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class GniStatus000(GwStrEnum):
    Unknown = auto()
    Pending = auto()
    Active = auto()
    Done = auto()

    @classmethod
    def default(cls) -> "GniStatus000":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class GniStatusMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> GniStatus:
        if not GniStatus000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to GniStatus000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, GniStatus, GniStatus.default())

    @classmethod
    def local_to_type(cls, gni_status: GniStatus) -> str:
        if not isinstance(gni_status, GniStatus):
            raise SchemaError(f"{gni_status} must be of type {GniStatus}")
        versioned_enum = as_enum(gni_status, GniStatus000, GniStatus000.default())
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, GniStatus000] = {
        "00000000": GniStatus000.Unknown,
        "7890ab0a": GniStatus000.Pending,
        "69241259": GniStatus000.Active,
        "8222421f": GniStatus000.Done,
    }

    versioned_enum_to_type_dict: Dict[GniStatus000, str] = {
        GniStatus000.Unknown: "00000000",
        GniStatus000.Pending: "7890ab0a",
        GniStatus000.Active: "69241259",
        GniStatus000.Done: "8222421f",
    }


class StrategyName001SchemaEnum:
    enum_name: str = "strategy.name.001"
    symbols: List[str] = [
        "00000000",
        "642c83d3",
        "4bb2cf7e",
        "f5961401",
        "73fbe6ab",
        "5e18a52e",
        "b2a125d6",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class StrategyName001(GwStrEnum):
    NoActor = auto()
    WorldA = auto()
    SupervisorA = auto()
    AtnHeatPumpWithBoostStore = auto()
    TcGlobalA = auto()
    MarketMakerA = auto()
    AtnBrickStorageHeater = auto()

    @classmethod
    def default(cls) -> "StrategyName001":
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class StrategyNameMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> StrategyName:
        if not StrategyName001SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to StrategyName001 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, StrategyName, StrategyName.default())

    @classmethod
    def local_to_type(cls, strategy_name: StrategyName) -> str:
        if not isinstance(strategy_name, StrategyName):
            raise SchemaError(f"{strategy_name} must be of type {StrategyName}")
        versioned_enum = as_enum(
            strategy_name, StrategyName001, StrategyName001.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, StrategyName001] = {
        "00000000": StrategyName001.NoActor,
        "642c83d3": StrategyName001.WorldA,
        "4bb2cf7e": StrategyName001.SupervisorA,
        "f5961401": StrategyName001.AtnHeatPumpWithBoostStore,
        "73fbe6ab": StrategyName001.TcGlobalA,
        "5e18a52e": StrategyName001.MarketMakerA,
        "b2a125d6": StrategyName001.AtnBrickStorageHeater,
    }

    versioned_enum_to_type_dict: Dict[StrategyName001, str] = {
        StrategyName001.NoActor: "00000000",
        StrategyName001.WorldA: "642c83d3",
        StrategyName001.SupervisorA: "4bb2cf7e",
        StrategyName001.AtnHeatPumpWithBoostStore: "f5961401",
        StrategyName001.TcGlobalA: "73fbe6ab",
        StrategyName001.MarketMakerA: "5e18a52e",
        StrategyName001.AtnBrickStorageHeater: "b2a125d6",
    }


def check_is_reasonable_unix_time_s(v: int) -> None:
    """
    ReasonableUnixTimeS format: time in unix seconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeS format
    """
    from datetime import datetime, timezone
    start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(3000, 1, 1, tzinfo=timezone.utc)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    if v < start_timestamp:
        raise ValueError(f"{v} must be after Jan 1 2000")
    if v > end_timestamp:
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


class GNodeInstanceGt(BaseModel):
    """Used to send and receive updates about GNodeInstances.

    One of the layers of abstraction connecting a GNode with a running app in
    a Docker container.

    [More info](https://gridworks.readthedocs.io/en/latest/g-node-instance.html).
    """

    GNodeInstanceId: str = Field(
        title="Immutable identifier for GNodeInstance (Gni)",
    )
    GNode: GNodeGt = Field(
        title="The GNode represented by the Gni",
    )
    Strategy: StrategyName = Field(
        title="Used to determine the code running in a GNode actor application",
    )
    Status: GniStatus = Field(
        title="Lifecycle Status for Gni",
    )
    SupervisorContainerId: str = Field(
        title="The Id of the docker container where the Gni runs",
    )
    StartTimeUnixS: int = Field(
        title="When the gni starts representing the GNode",
        description="Specifically, when the Status changes from Pending to Active. Note that this is time in the GNode's World, which may not be real time if it is a simulation.",
    )
    EndTimeUnixS: int = Field(
        title="When the gni stops representing the GNode",
        description="Specifically, when the Status changes from Active to Done.",
    )
    AlgoAddress: Optional[str] = Field(
        title="Algorand address for Gni",
        default=None,
    )
    TypeName: Literal["g.node.instance.gt"] = "g.node.instance.gt"
    Version: str = "000"

    @validator("GNodeInstanceId")
    def _check_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"GNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("Strategy")
    def _check_strategy(cls, v: StrategyName) -> StrategyName:
        return as_enum(v, StrategyName, StrategyName.NoActor)

    @validator("Status")
    def _check_status(cls, v: GniStatus) -> GniStatus:
        return as_enum(v, GniStatus, GniStatus.Unknown)

    @validator("SupervisorContainerId")
    def _check_supervisor_container_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"SupervisorContainerId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("StartTimeUnixS")
    def _check_start_time_unix_s(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_s(v)
        except ValueError as e:
            raise ValueError(
                f"StartTimeUnixS failed ReasonableUnixTimeS format validation: {e}"
            )
        return v

    @validator("AlgoAddress")
    def _check_algo_address(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        try:
            check_is_algo_address_string_format(v)
        except ValueError as e:
            raise ValueError(
                f"AlgoAddress failed AlgoAddressStringFormat format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["GNode"] = self.GNode.as_dict()
        del d["Strategy"]
        Strategy = as_enum(self.Strategy, StrategyName, StrategyName.default())
        d["StrategyGtEnumSymbol"] = StrategyNameMap.local_to_type(Strategy)
        del d["Status"]
        Status = as_enum(self.Status, GniStatus, GniStatus.default())
        d["StatusGtEnumSymbol"] = GniStatusMap.local_to_type(Status)
        if d["AlgoAddress"] is None:
            del d["AlgoAddress"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class GNodeInstanceGt_Maker:
    type_name = "g.node.instance.gt"
    version = "000"

    def __init__(
        self,
        g_node_instance_id: str,
        g_node: GNodeGt,
        strategy: StrategyName,
        status: GniStatus,
        supervisor_container_id: str,
        start_time_unix_s: int,
        end_time_unix_s: int,
        algo_address: Optional[str],
    ):
        self.tuple = GNodeInstanceGt(
            GNodeInstanceId=g_node_instance_id,
            GNode=g_node,
            Strategy=strategy,
            Status=status,
            SupervisorContainerId=supervisor_container_id,
            StartTimeUnixS=start_time_unix_s,
            EndTimeUnixS=end_time_unix_s,
            AlgoAddress=algo_address,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GNodeInstanceGt) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GNodeInstanceGt:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> GNodeInstanceGt:
        d2 = dict(d)
        if "GNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeInstanceId")
        if "GNode" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNode")
        if not isinstance(d2["GNode"], dict):
            raise SchemaError(f"d['GNode'] {d2['GNode']} must be a GNodeGt!")
        g_node = GNodeGt_Maker.dict_to_tuple(d2["GNode"])
        d2["GNode"] = g_node
        if "StrategyGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StrategyGtEnumSymbol")
        if d2["StrategyGtEnumSymbol"] in StrategyName001SchemaEnum.symbols:
            d2["Strategy"] = StrategyNameMap.type_to_local(d2["StrategyGtEnumSymbol"])
        else:
            d2["Strategy"] = StrategyName.default()
        if "StatusGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StatusGtEnumSymbol")
        if d2["StatusGtEnumSymbol"] in GniStatus000SchemaEnum.symbols:
            d2["Status"] = GniStatusMap.type_to_local(d2["StatusGtEnumSymbol"])
        else:
            d2["Status"] = GniStatus.default()
        if "SupervisorContainerId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SupervisorContainerId")
        if "StartTimeUnixS" not in d2.keys():
            raise SchemaError(f"dict {d2} missing StartTimeUnixS")
        if "EndTimeUnixS" not in d2.keys():
            raise SchemaError(f"dict {d2} missing EndTimeUnixS")
        if "AlgoAddress" not in d2.keys():
            d2["AlgoAddress"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return GNodeInstanceGt(
            GNodeInstanceId=d2["GNodeInstanceId"],
            GNode=d2["GNode"],
            Strategy=d2["Strategy"],
            Status=d2["Status"],
            SupervisorContainerId=d2["SupervisorContainerId"],
            StartTimeUnixS=d2["StartTimeUnixS"],
            EndTimeUnixS=d2["EndTimeUnixS"],
            AlgoAddress=d2["AlgoAddress"],
            TypeName=d2["TypeName"],
            Version="000",
        )

    @classmethod
    def tuple_to_dc(cls, t: GNodeInstanceGt) -> GNodeInstance:
        if t.GNodeInstanceId in GNodeInstance.by_id.keys():
            dc = GNodeInstance.by_id[t.GNodeInstanceId]
        else:
            dc = GNodeInstance(
                g_node_instance_id=t.GNodeInstanceId,
                g_node=GNodeGt_Maker.tuple_to_dc(t.GNode),
                strategy=t.Strategy,
                status=t.Status,
                supervisor_container_id=t.SupervisorContainerId,
                start_time_unix_s=t.StartTimeUnixS,
                end_time_unix_s=t.EndTimeUnixS,
                algo_address=t.AlgoAddress,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: GNodeInstance) -> GNodeInstanceGt:
        t = GNodeInstanceGt_Maker(
            g_node_instance_id=dc.g_node_instance_id,
            g_node=GNodeGt_Maker.dc_to_tuple(dc.g_node),
            strategy=dc.strategy,
            status=dc.status,
            supervisor_container_id=dc.supervisor_container_id,
            start_time_unix_s=dc.start_time_unix_s,
            end_time_unix_s=dc.end_time_unix_s,
            algo_address=dc.algo_address,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> GNodeInstance:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: GNodeInstance) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> GNodeInstance:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
