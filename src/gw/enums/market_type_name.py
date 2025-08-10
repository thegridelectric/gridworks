from enum import auto
from typing import List
from gw.enums import GwStrEnum


class MarketTypeName(GwStrEnum):
    """
    Categorizes different markets run by MarketMaker
    Values:
      - unknown: Default unknown
      - rt5gate5: Real-time energy, 5 minute MarketSlots, gate closing 5 minutes prior to 
        start
      - rt60gate5: Real-time energy, 60 minute MarketSlots, gate closing 5 minutes prior to 
        start
      - da60: Day-ahead energy, 60 minute MarketSlots
      - rt60gate30: Real-time energy, 60 minute MarketSlots, gate closing 30 minutes prior 
        to start
      - rt15gate5: Real-time energy, 15 minute MarketSlots, gate closing 5 minutes prior to 
        start
      - rt30gate5: Real-time energy, 30 minute MarketSlots, gate closing 5 minutes prior to 
        start
      - rt60gate30b: Real-time energy, 30 minute MarketSlots, gate closing 5 minutes prior to 
        start, QuantityUnit AvgkW

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/market.type.name.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
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
        return cls.unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "market.type.name"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
