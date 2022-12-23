from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MessageCategory(StrEnum):
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
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
