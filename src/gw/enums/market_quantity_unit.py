from enum import auto
from typing import List

from gw.enums import GwStrEnum


class MarketQuantityUnit(GwStrEnum):
    """
    Quantity unit assigned to MarketMaker MarketType

    Choices and descriptions:

      * AvgMW:
      * AvgkW:
    """

    AvgMW = auto()
    AvgkW = auto()

    @classmethod
    def default(cls) -> "MarketQuantityUnit":
        """
        Returns default value AvgMW
        """
        return cls.AvgMW

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
