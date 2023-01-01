from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class GNodeRole(StrEnum):
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

    @classmethod
    def default(cls) -> "GNodeRole":
        return cls.GNode

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
