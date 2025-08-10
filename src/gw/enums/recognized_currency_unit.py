from enum import auto
from typing import List
from gw.enums import GwStrEnum


class RecognizedCurrencyUnit(GwStrEnum):
    """
    Unit of currency
    Values:
      - Unknown
      - USD: US Dollar
      - GBP: Pounds sterling

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/recognized.currency.unit.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    UNKNOWN = auto()
    USD = auto()
    GBP = auto()

    @classmethod
    def default(cls) -> "RecognizedCurrencyUnit":
        return cls.UNKNOWN

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "recognized.currency.unit"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
