from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MarketPriceUnit(StrEnum):
    """
    Price unit assigned to MarketMaker MarketType

    Choices and descriptions:

      * USDPerMWh:
    """

    USDPerMWh = auto()

    @classmethod
    def default(cls) -> "MarketPriceUnit":
        """
        Returns default value USDPerMWh
        """
        return cls.USDPerMWh

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
