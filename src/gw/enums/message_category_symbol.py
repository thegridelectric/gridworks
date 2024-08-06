from enum import auto
from typing import List
from typing import Optional

from gw.enums import GwStrEnum


class MessageCategorySymbol(GwStrEnum):
    """
    Shorthand symbols for MessageCategory000 Enum, used in meta-data like routing
        keys

    Enum message.category.symbol version 000 in the GridWorks Type registry.

    Used by used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#messagecategorysymbol)

    Values (with symbols in parens):
      - unknown (00000000): Default value
      - rj (7e4957a3): Serialized Json message sent on the world rabbit broker from one GNode
        actor to another
      - rjb (68bb105c): Serailized Json message broadcast on the world rabbit broker by a GNode
        actor
      - s (eb802736): GwSerial protocol message sent on the world rabbit broker
      - gw (f36a8e69): Serialized Json message following MQTT topic format, sent on the world
        rabbit broker
      - post (94329f30): REST API post
      - postack (9fc1b9d4): REST API post response
      - get (8c36344a): REST API GET
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
        Returns default value (in this case unknown)
        """
        return cls.unknown

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
            raise ValueError("This method applies to strings, not enums")
        if value not in value_to_version.keys():
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (message.category.symbol)
        """
        return "message.category.symbol"

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
            a later version of this enum, returns the default value of "unknown".
        """
        if symbol not in symbol_to_value.keys():
            return cls.default().value
        return symbol_to_value[symbol]

    @classmethod
    def value_to_symbol(cls, value: str) -> str:
        """
        Provides the encoding symbol for a MessageCategorySymbol enum to send in seriliazed messages.

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
            "7e4957a3",
            "68bb105c",
            "eb802736",
            "f36a8e69",
            "94329f30",
            "9fc1b9d4",
            "8c36344a",
        ]


symbol_to_value = {
    "00000000": "unknown",
    "7e4957a3": "rj",
    "68bb105c": "rjb",
    "eb802736": "s",
    "f36a8e69": "gw",
    "94329f30": "post",
    "9fc1b9d4": "postack",
    "8c36344a": "get",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "unknown": "000",
    "rj": "000",
    "rjb": "000",
    "s": "000",
    "gw": "000",
    "post": "000",
    "postack": "000",
    "get": "000",
}
