from enum import auto
from typing import List
from typing import Optional

from gw.enums import GwStrEnum


class MessageCategory(GwStrEnum):
    """
    Categorizes how GridWorks messages are sent and decoded/encoded

    Enum message.category version 000 in the GridWorks Type registry.

    Used by used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#messagecategory)

    Values (with symbols in parens):
      - Unknown (00000000): Default value
      - RabbitJsonDirect (9057ab24): Serialized Json message sent on the world rabbit broker from one GNode
        actor to another
      - RabbitJsonBroadcast (7813eb50): Serailized Json message broadcast on the world rabbit broker by a GNode
        actor
      - RabbitGwSerial (9d70744e): GwSerial protocol message sent on the world rabbit broker
      - MqttJsonBroadcast (16594e91): Serialized Json message following MQTT topic format, sent on the world
        rabbit broker
      - RestApiPost (5b2c69cb): REST API post
      - RestApiPostResponse (7cbba191): REST API post response
      - RestApiGet (167236a6): REST API GET
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
        Returns default value (in this case Unknown)
        """
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]

    @classmethod
    def version(cls, value: Optional[str] = None) -> str:
        """
        Returns the version of the class (default) used by this package or the
        version of a candidate enum value (always less than or equal to the version
        of the class)

        Args:
            value (Optional[str]): None (for version of the Enum itself) or
            the candidate enum value.

        Raises:
            ValueError: If the value is not one of the enum values.

        Returns:
            str: The version of the enum used by this code (if given no
            value) OR the earliest version of the enum containing the value.
        """
        if value is None:
            return "000"
        if not isinstance(value, str):
            raise ValueError(f"This method applies to strings, not enums")
        if value not in value_to_version.keys():
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (message.category)
        """
        return "message.category"

    @classmethod
    def enum_version(cls) -> str:
        """
        The version in the GridWorks Type Registry (000)
        """
        return "000"

    @classmethod
    def symbol_to_value(cls, symbol: str) -> str:
        """
        Given the symbol sent in a serialized message, returns the encoded enum.

        Args:
            symbol (str): The candidate symbol.

        Returns:
            str: The encoded value associated to that symbol. If the symbol is not
            recognized - which could happen if the actor making the symbol is using
            a later version of this enum, returns the default value of "Unknown".
        """
        if symbol not in symbol_to_value.keys():
            return cls.default().value
        return symbol_to_value[symbol]

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        """
        Provides the encoding symbol for a MessageCategory enum to send in seriliazed messages.

        Args:
            symbol (str): The candidate value.

        Returns:
            str: The symbol encoding that value. If the value is not recognized -
            which could happen if the actor making the message used a later version
            of this enum than the actor decoding the message, returns the default
            symbol of "00000000".
        """
        if value not in value_to_symbol.keys():
            return value_to_symbol[cls.default().value]
        return value_to_symbol[value]

    @classmethod
    def symbols(cls) -> List[str]:
        """
        Returns a list of the enum symbols
        """
        return [
            "00000000",
            "9057ab24",
            "7813eb50",
            "9d70744e",
            "16594e91",
            "5b2c69cb",
            "7cbba191",
            "167236a6",
        ]


symbol_to_value = {
    "00000000": "Unknown",
    "9057ab24": "RabbitJsonDirect",
    "7813eb50": "RabbitJsonBroadcast",
    "9d70744e": "RabbitGwSerial",
    "16594e91": "MqttJsonBroadcast",
    "5b2c69cb": "RestApiPost",
    "7cbba191": "RestApiPostResponse",
    "167236a6": "RestApiGet",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "Unknown": "000",
    "RabbitJsonDirect": "000",
    "RabbitJsonBroadcast": "000",
    "RabbitGwSerial": "000",
    "MqttJsonBroadcast": "000",
    "RestApiPost": "000",
    "RestApiPostResponse": "000",
    "RestApiGet": "000",
}
