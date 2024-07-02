"""
Tests for enum market.quantity.unit.000 from the GridWorks Type Registry.
"""

from gw.enums import MarketQuantityUnit


def test_market_quantity_unit() -> None:
    assert set(MarketQuantityUnit.values()) == {
        "AvgMW",
        "AvgkW",
    }

    assert MarketQuantityUnit.default() == MarketQuantityUnit.AvgMW
    assert MarketQuantityUnit.enum_name() == "market.quantity.unit"
    assert MarketQuantityUnit.enum_version() == "000"

    assert MarketQuantityUnit.version("AvgMW") == "000"
    assert MarketQuantityUnit.version("AvgkW") == "000"

    for value in MarketQuantityUnit.values():
        symbol = MarketQuantityUnit.value_to_symbol(value)
        assert MarketQuantityUnit.symbol_to_value(symbol) == value
