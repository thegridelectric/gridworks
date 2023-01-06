from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MessageCategorySymbol(StrEnum):
    """
    Shorthand symbols for MessageCategory000 Enum, used in meta-data like routing keys

    Choices and descriptions:

      * unknown: Default value
      * rj: Serialized Json message sent on the world rabbit broker from one GNode actor to another
      * rjb: Serailized Json message broadcast on the world rabbit broker by a GNode actor
      * s: GwSerial protocol message sent on the world rabbit broker
      * gw: Serialized Json message following MQTT topic format, sent on the world rabbit broker
      * post: REST API post
      * postack: REST API post response
      * get: REST API GET
    """

    unknown = auto()
    rj = auto()
    rjb = auto()
    s = auto()
    gw = auto()
    post = auto()
    postack = auto()
    get = auto()

    @classmethod
    def default(cls) -> "MessageCategorySymbol":
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
