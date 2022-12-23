from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class StrategyName(StrEnum):
    NoActor = auto()
    WorldA = auto()
    SupervisorA = auto()
    AtnHeatPumpWithBoostStore = auto()
    TcGlobalA = auto()
    MarketMakerA = auto()

    @classmethod
    def default(cls) -> "StrategyName":
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
