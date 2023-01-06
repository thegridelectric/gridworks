from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class StrategyName(StrEnum):
    """
    Used to assign code to run a particular GNodeInstance

    Choices and descriptions:

      * NoActor: Assigned to GNodes that do not have actors
      * WorldA: Basic GridWorks world strategy
      * SupervisorA: Supervisor A Strategy, in [gridworks-atn package](https://pypi.org/project/gridworks-atn/)
      * AtnHeatPumpWithBoostStore: GridWorks strategy for an AtomicTNode representing a type of heat pump storage heating system
      * TcGlobalA: Basic GridWorks TimeCoordinator strategy, in [gridworks-timecoordinator repo](https://github.com/thegridelectric/gridworks-timecoordinator)
      * MarketMakerA: Simple GridWorks MarketMaker strategy, in [gridworks-marketmaker repo](https://github.com/thegridelectric/gridworks-marketmaker)
    """

    NoActor = auto()
    WorldA = auto()
    SupervisorA = auto()
    AtnHeatPumpWithBoostStore = auto()
    TcGlobalA = auto()
    MarketMakerA = auto()

    @classmethod
    def default(cls) -> "StrategyName":
        """
        Returns default value NoActor
        """
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
