"""
Tests for enum market.type.name.000 from the GridWorks Type Registry.
"""

from gw.enums import MarketTypeName


def test_market_type_name() -> None:
    assert set(MarketTypeName.values()) == {
        "unknown",
        "rt5gate5",
        "rt60gate5",
        "da60",
        "rt60gate30",
        "rt15gate5",
        "rt30gate5",
        "rt60gate30b",
    }

    assert MarketTypeName.default() == MarketTypeName.unknown
    assert MarketTypeName.enum_name() == "market.type.name"
    assert MarketTypeName.enum_version() == "000"

    assert MarketTypeName.version("unknown") == "000"
    assert MarketTypeName.version("rt5gate5") == "000"
    assert MarketTypeName.version("rt60gate5") == "000"
    assert MarketTypeName.version("da60") == "000"
    assert MarketTypeName.version("rt60gate30") == "000"
    assert MarketTypeName.version("rt15gate5") == "000"
    assert MarketTypeName.version("rt30gate5") == "000"
    assert MarketTypeName.version("rt60gate30b") == "000"

    for value in MarketTypeName.values():
        symbol = MarketTypeName.value_to_symbol(value)
        assert MarketTypeName.symbol_to_value(symbol) == value
