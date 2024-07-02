from enum import auto
from typing import List
from typing import Optional

from gw.enums import GwStrEnum


class MarketTypeName(GwStrEnum):
    """
    Categorizes different markets run by MarketMaker

    Enum market.type.name version 000 in the GridWorks Type registry.

    Used by used by multiple Application Shared Languages (ASLs). For more information:
      - [ASLs](https://gridworks-type-registry.readthedocs.io/en/latest/)
      - [Global Authority](https://gridworks-type-registry.readthedocs.io/en/latest/enums.html#markettypename)

    Values (with symbols in parens):
      - unknown (00000000): Default unknown
      - rt5gate5 (d20b81e4): Real-time energy, 5 minute MarketSlots, gate closing 5 minutes prior to
        start
      - rt60gate5 (b36cbfb4): Real-time energy, 60 minute MarketSlots, gate closing 5 minutes prior to
        start
      - da60 (94a3fe9b): Day-ahead energy, 60 minute MarketSlots
      - rt60gate30 (5f335bdb): Real-time energy, 60 minute MarketSlots, gate closing 30 minutes prior
        to start
      - rt15gate5 (01a84101): Real-time energy, 15 minute MarketSlots, gate closing 5 minutes prior to
        start
      - rt30gate5 (e997ccfb): Real-time energy, 30 minute MarketSlots, gate closing 5 minutes prior to
        start
      - rt60gate30b (618f9c0a): Real-time energy, 30 minute MarketSlots, gate closing 5 minutes prior to
        start, QuantityUnit AvgkW
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
            raise ValueError(f"This method applies to strings, not enums")
        if value not in value_to_version.keys():
            raise ValueError(f"Unknown enum value: {value}")
        return value_to_version[value]

    @classmethod
    def enum_name(cls) -> str:
        """
        The name in the GridWorks Type Registry (market.type.name)
        """
        return "market.type.name"

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
        Provides the encoding symbol for a MarketTypeName enum to send in seriliazed messages.

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
            "d20b81e4",
            "b36cbfb4",
            "94a3fe9b",
            "5f335bdb",
            "01a84101",
            "e997ccfb",
            "618f9c0a",
        ]


symbol_to_value = {
    "00000000": "unknown",
    "d20b81e4": "rt5gate5",
    "b36cbfb4": "rt60gate5",
    "94a3fe9b": "da60",
    "5f335bdb": "rt60gate30",
    "01a84101": "rt15gate5",
    "e997ccfb": "rt30gate5",
    "618f9c0a": "rt60gate30b",
}

value_to_symbol = {value: key for key, value in symbol_to_value.items()}

value_to_version = {
    "unknown": "000",
    "rt5gate5": "000",
    "rt60gate5": "000",
    "da60": "000",
    "rt60gate30": "000",
    "rt15gate5": "000",
    "rt30gate5": "000",
    "rt60gate30b": "000",
}
