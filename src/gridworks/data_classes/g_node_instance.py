""" GNode DataClass Definition """
import logging
from typing import Dict
from typing import List
from typing import Optional

from gridworks.data_classes.g_node import GNode
from gridworks.data_classes.gps_point import GpsPoint
from gridworks.enums import GniStatus
from gridworks.enums import GNodeRole
from gridworks.enums import GNodeStatus
from gridworks.enums import StrategyName
from gridworks.errors import DcError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class GNodeInstance:
    by_id: Dict[str, "GNodeInstance"] = {}
    by_alias: Dict[str, "GNodeInstance"] = {}

    def __new__(cls, g_node_instance_id: str, *args, **kwargs) -> "GNodeInstance":  # type: ignore
        try:
            return cls.by_id[g_node_instance_id]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[g_node_instance_id] = instance
            return instance

    def __init__(
        self,
        g_node_instance_id: str,
        g_node: GNode,
        strategy: StrategyName,
        status: GniStatus,
        supervisor_container_id: str,
        start_time_unix_s: int,
        end_time_unix_s: int = 0,
        algo_address: Optional[str] = None,
    ):
        self.g_node_instance_id = g_node_instance_id
        if not isinstance(g_node, GNode):
            raise DcError(f"g_node {g_node} must be GNode, got {type(g_node)}")
        self.g_node: GNode = g_node
        if not isinstance(strategy, StrategyName):
            raise DcError(
                f"strategy {strategy} must be StrategyName, got {type(strategy)}"
            )

        self.strategy: StrategyName = strategy
        if not isinstance(status, GniStatus):
            raise DcError(f"status {status} must be GniStatus, got {type(status)}")
        self.status: GniStatus = status
        self.supervisor_container_id: str = supervisor_container_id
        self.start_time_unix_s: int = start_time_unix_s
        self.end_time_unix_s: int = end_time_unix_s
        self.algo_address: Optional[str] = algo_address

        self.__class__.by_alias[self.g_node.alias] = self

    #####################################################
    # With the exception of Status, all attributes of a GNode
    # come through as properties for the GNodeInstance. e.g.
    # gni.alias instead of gni.g_node.alias in the code
    #####################################################

    @property
    def g_node_id(self) -> str:
        return self.g_node.g_node_id

    @property
    def alias(self) -> str:
        return self.g_node.alias

    @property
    def role(self) -> GNodeRole:
        return self.g_node.role

    @property
    def g_node_registry_addr(self) -> str:
        return self.g_node.g_node_registry_addr

    @property
    def prev_alias(self) -> Optional[str]:
        return self.g_node.prev_alias

    @property
    def gps_point_id(self) -> Optional[str]:
        return self.g_node.gps_point_id

    @property
    def ownership_deed_nft_id(self) -> Optional[int]:
        return self.g_node.ownership_deed_nft_id

    @property
    def ownership_deed_validator_addr(self) -> Optional[str]:
        return self.g_node.ownership_deed_validator_addr

    @property
    def owner_addr(self) -> Optional[str]:
        return self.g_node.owner_addr

    @property
    def daemon_addr(self) -> Optional[str]:
        return self.g_node.daemon_addr

    @property
    def trading_rights_nft_id(self) -> Optional[int]:
        return self.g_node.trading_rights_nft_id

    @property
    def component_id(self) -> Optional[str]:
        return self.g_node.component_id

    @property
    def display_name(self) -> Optional[str]:
        return self.g_node.display_name

    def gps_point(self) -> Optional[GpsPoint]:
        if self.gps_point_id is None:
            return None
        return GpsPoint.by_id["gps_point_id"]

    def is_root(self) -> bool:
        alias_list = self.alias.split(".")
        alias_list.pop()
        if len(alias_list) == 0:
            return True
        return False

    @classmethod
    def active_gnis(cls) -> List["GNodeInstance"]:
        gnis = list(GNodeInstance.by_alias.values())
        return list(filter(lambda x: x.g_node.status == GNodeStatus.Active, gnis))

    @classmethod
    def parent_from_alias(cls, alias: str) -> Optional["GNodeInstance"]:
        """
        Returns:
            - GNode. If the parent as suggested by the alias exists as an
            Active BaseGNode, returns that.
            - None. If alias is one word long (i.e. root of world)
        """
        alias_list = alias.split(".")
        alias_list.pop()
        parent_alias = ".".join(alias_list)
        if parent_alias in list(map(lambda x: x.alias, cls.active_gnis())):
            return GNodeInstance.by_alias[parent_alias]
        return None

    def parent(self) -> Optional["GNodeInstance"]:
        """
        Raises: DcError if "natural" parent (as suggested by alias) is not Active,
        and either
            - prev_alias is None, OR
            - the parent as suggested by prev_alias is not Active and/or
            does not exist.
        Returns:
            BaseGNode.   Parent BaseGNode
              - If the parent as suggested by the alias exists as an
            Active GNode, returns that ("natural" parent)
              - Else, if the parent as suggested by the prev_alais exists
              as an active GNode, returns that.
            None.
              - If alias is one word long (i.e. root of world)
        """
        if self.is_root():
            return None
        natural_parent = self.parent_from_alias(self.alias)
        if natural_parent is not None:
            return natural_parent

        # alias may point to incorrect parent if getting updated
        if self.prev_alias is None:
            raise DcError(f"error finding parent for {self.alias}!")

        parent_pending_alias_update = self.parent_from_alias(self.prev_alias)
        if parent_pending_alias_update is None:
            raise DcError(f"error finding parent for {self.alias}!")
        return parent_pending_alias_update

    def children(self) -> List["GNodeInstance"]:
        """Returns the list of BaseGnodes identifying this node as parent"""
        return list(
            filter(lambda x: x.parent() == self, GNodeInstance.by_alias.values())
        )
