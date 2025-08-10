from enum import auto
from typing import List
from gw.enums import GwStrEnum


class MessageCategory(GwStrEnum):
    """
    Categorizes message delivery patterns for ASL types. See [Message Delivery
        Architecture](https://gridworks.readthedocs.io/message-delivery-architecture/)
        for details.
    Values:
      - Unknown: Default value when message pattern cannot be determined
      - JsonDirect: Point-to-point delivery between specific actors
        Use for: commands, responses, targeted telemetry
      - JsonBroadcast: One-to-many delivery to multiple recipients
        Use for: market updates, price and weather forecasts, shared data
      - ScadaWrapped: Messages sent from SCADA systems that may require acknowledgement tracking
      - Serial: Bandwidth-optimized binary format (future)
        Use for: resource-constrained scenarios, high-frequency data

    For more information:
        - [ASL Definition](https://raw.githubusercontent.com/thegridelectric/gridworks-asl/refs/heads/dev/type_definitions/enums/message.category.000.yaml)
        - [GridWorks ASL Docs](https://gridworks-asl.readthedocs.io)
    """

    Unknown = auto()
    JsonDirect = auto()
    JsonBroadcast = auto()
    ScadaWrapped = auto()
    Serial = auto()

    @classmethod
    def default(cls) -> "MessageCategory":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]

    @classmethod
    def enum_name(cls) -> str:
        return "message.category"

    @classmethod
    def enum_version(cls) -> str:
        return "000"
