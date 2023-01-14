from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MarketTypeName(StrEnum):
    """
    Categorizes different markets run by MarketMaker

    Choices and descriptions:

      * unknown: Default unknown
      * rt5gate5: Real-time energy, 5 minute MarketSlots, gate closing 5 minutes prior to start
      * rt60gate5: Real-time energy, 60 minute MarketSlots, gate closing 5 minutes prior to start
      * da60: Day-ahead energy, 60 minute MarketSlots
      * rt60gate30: Real-time energy, 60 minute MarketSlots, gate closing 30 minutes prior to start
      * rt15gate5: Real-time energy, 15 minute MarketSlots, gate closing 5 minutes prior to start
      * rt30gate5: Real-time energy, 30 minute MarketSlots, gate closing 5 minutes prior to start
      * rt60gate30b: Real-time energy, 30 minute MarketSlots, gate closing 5 minutes prior to start, QuantityUnit AvgkW
    """

    unknown = auto()
    rt5gate5 = auto()
    rt60gate5 = auto()
    da60 = auto()
    rt60gate30 = auto()
    rt15gate5 = auto()
    rt30gate5 = auto()
    rt60gate30b = auto()

    @classmethod
    def default(cls) -> "MarketTypeName":
        """
        Returns default value unknown
        """
        return cls.unknown

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
