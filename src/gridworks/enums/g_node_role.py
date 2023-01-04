from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class GNodeRole(StrEnum):
    """Doc string for GNodeRole"""

    GNode = auto()
    TerminalAsset = auto()
    Scada = auto()
    PriceService = auto()
    AggregatedTNode = auto()
    WeatherService = auto()
    AtomicTNode = auto()
    MarketMaker = auto()
    AtomicMeteringNode = auto()
    ConductorTopologyNode = auto()
    InterconnectionComponent = auto()
    World = auto()
    TimeCoordinator = auto()
    Supervisor = auto()

    def sample_method(self) -> None:
        """This is a sample method"""
        pass

    @classmethod
    def default(cls) -> "GNodeRole":
        """Default docstring"""
        return cls.GNode

    @classmethod
    def values(cls) -> List[str]:
        """values docstring"""
        return [elt.value for elt in cls]
