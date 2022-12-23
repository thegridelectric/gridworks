""" GNode DataClass Definition """
import logging
from typing import Dict
from typing import List
from typing import Optional

from gridworks.data_classes.gps_point import GpsPoint
from gridworks.enums import GNodeRole
from gridworks.enums import GNodeStatus
from gridworks.errors import DcError


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class GNode:
    by_id: Dict[str, "GNode"] = {}
    by_alias: Dict[str, "GNode"] = {}

    def __new__(cls, g_node_id: str, *args, **kwargs) -> "GNode":  # type: ignore
        try:
            return cls.by_id[g_node_id]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[g_node_id] = instance
            return instance

    def __init__(
        self,
        g_node_id: str,
        alias: str,
        status: GNodeStatus,
        role: GNodeRole,
        g_node_registry_addr: str,
        prev_alias: Optional[str] = None,
        gps_point_id: Optional[str] = None,
        ownership_deed_nft_id: Optional[int] = None,
        ownership_deed_validator_addr: Optional[str] = None,
        owner_addr: Optional[str] = None,
        daemon_addr: Optional[str] = None,
        trading_rights_nft_id: Optional[int] = None,
        component_id: Optional[str] = None,
        display_name: Optional[str] = None,
    ):
        self.g_node_id = g_node_id
        self.alias = alias
        if not isinstance(status, GNodeStatus):
            raise DcError(f"status {status} must be GNodeStatus, got {type(status)}")
        self.status: GNodeStatus = status
        if not isinstance(role, GNodeRole):
            raise DcError(f"role {role} must be  GNodeRole, got {type(role)}")
        self.role: GNodeRole = role
        self.g_node_registry_addr = g_node_registry_addr
        self.prev_alias = prev_alias
        self.gps_point_id = gps_point_id
        self.ownership_deed_nft_id = ownership_deed_nft_id
        self.ownership_deed_validator_addr = ownership_deed_validator_addr
        self.owner_addr = owner_addr
        self.daemon_addr = daemon_addr
        self.trading_rights_nft_id = trading_rights_nft_id
        self.component_id = component_id
        self.display_name = display_name
        self.__class__.by_alias[self.alias] = self

    def __repr__(self) -> str:
        rs = f"GNode Alias: {self.alias}, Role: {self.role.value}, Status: {self.status.value}"
        if self.ownership_deed_nft_id and self.role == GNodeRole.TerminalAsset:
            rs += f", TaDeedIdx: {self.ownership_deed_nft_id}"
        return rs

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
    def active_g_nodes(cls) -> List["GNode"]:
        g_nodes = list(GNode.by_alias.values())
        return list(filter(lambda x: x.status == GNodeStatus.Active, g_nodes))

    @classmethod
    def parent_from_alias(cls, alias: str) -> Optional["GNode"]:
        """
        Returns:
            - GNode. If the parent as suggested by the alias exists as an
            Active BaseGNode, returns that.
            - None. If alias is one word long (i.e. root of world)
        """
        alias_list = alias.split(".")
        alias_list.pop()
        parent_alias = ".".join(alias_list)
        if parent_alias in list(map(lambda x: x.alias, cls.active_g_nodes())):
            return GNode.by_alias[parent_alias]
        return None

    def parent(self) -> Optional["GNode"]:
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

    def children(self) -> List["GNode"]:
        """Returns the list of BaseGnodes identifying this node as parent"""
        return list(filter(lambda x: x.parent() == self, GNode.by_alias.values()))
