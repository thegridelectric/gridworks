from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class MessageCategory(GwStrEnum):
    """
    Categorizes how GridWorks messages are sent and decoded/encoded

    Choices and descriptions:

      * Unknown: Default value
      * RabbitJsonDirect: Serialized Json message sent on the world rabbit broker from one GNode actor to another
      * RabbitJsonBroadcast: Serailized Json message broadcast on the world rabbit broker by a GNode actor
      * RabbitGwSerial: GwSerial protocol message sent on the world rabbit broker
      * MqttJsonBroadcast: Serialized Json message following MQTT topic format, sent on the world rabbit broker
      * RestApiPost: REST API post
      * RestApiPostResponse: REST API post response
      * RestApiGet: REST API GET
    """

    Unknown = auto()
    RabbitJsonDirect = auto()
    RabbitJsonBroadcast = auto()
    RabbitGwSerial = auto()
    MqttJsonBroadcast = auto()
    RestApiPost = auto()
    RestApiPostResponse = auto()
    RestApiGet = auto()

    @classmethod
    def default(cls) -> "MessageCategory":
        """
        Returns default value Unknown
        """
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
