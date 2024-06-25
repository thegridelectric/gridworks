from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class RecognizedCurrencyUnit(GwStrEnum):
    """
    Unit of currency

    Choices and descriptions:

      * Unknown:
      * USD: US Dollar
      * GBP: Pounds sterling
    """

    UNKNOWN = auto()
    USD = auto()
    GBP = auto()

    @classmethod
    def default(cls) -> "RecognizedCurrencyUnit":
        """
        Returns default value UNKNOWN
        """
        return cls.UNKNOWN

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
