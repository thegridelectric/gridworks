from enum import auto
from typing import List
from gw.enums import GwStrEnum


class MessageCategorySymbol(GwStrEnum):
    """
    Shorthand symbols used as the first element in GridWorks routing keys. 
        See [Message Delivery Architecture](https://gridworks.readthedocs.io/message-delivery-architecture/) 
        for details.
    Values:
      - unknown: Default value when routing key parsing fails or symbol is not recognized
      - rj: JsonDirect - point-to-point messages. 
        Example: rj.hw1-keene-beech-scada.scada.power-watts.ltn.hw1-keene-beech
      - rjb: JsonBroadcast - One-to-many messages with optional radio channel targeting 
        Examples: 
          rjb.hw1-keene.marketmaker.market-list 
          rjb.hw1-keene.marketmaker.latest-price.rt60gate5
      - gw: ScadaWrapped - SCADA message with sckmowledgement tracking 
        Example: gw.hw1-keene-beech-scada.to.a.report-event
      - s: Serial - Future bandwidth-optimized format

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/message.category.symbol.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    unknown = auto()
    rj = auto()
    rjb = auto()
    gw = auto()
    s = auto()

    @classmethod
    def default(cls) -> "MessageCategorySymbol":
        return cls.unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "message.category.symbol"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
