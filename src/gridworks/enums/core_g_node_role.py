from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class CoreGNodeRole(GwStrEnum):
    """
    CoreGNodeRole assigned by GNodeFactory. [More Info](https://gridworks.readthedocs.io/en/latest/core-g-node-role.html).

    Choices and descriptions:

      * Other:
      * TerminalAsset:
      * AtomicTNode:
      * MarketMaker:
      * AtomicMeteringNode:
      * ConductorTopologyNode:
      * InterconnectionComponent:
      * Scada:
    """

    Other = auto()
    TerminalAsset = auto()
    AtomicTNode = auto()
    MarketMaker = auto()
    AtomicMeteringNode = auto()
    ConductorTopologyNode = auto()
    InterconnectionComponent = auto()
    Scada = auto()

    @classmethod
    def default(cls) -> "CoreGNodeRole":
        """
        Returns default value Other
        """
        return cls.Other

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
