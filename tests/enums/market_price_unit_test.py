"""
Tests for enum market.price.unit.000 from the GridWorks Type Registry.
"""

from gw.enums import MarketPriceUnit


def test_market_price_unit() -> None:
    assert set(MarketPriceUnit.values()) == {
        "USDPerMWh",
    }

    assert MarketPriceUnit.default() == MarketPriceUnit.USDPerMWh
    assert MarketPriceUnit.enum_name() == "market.price.unit"
    assert MarketPriceUnit.enum_version() == "000"

    assert MarketPriceUnit.version("USDPerMWh") == "000"

    for value in MarketPriceUnit.values():
        symbol = MarketPriceUnit.value_to_symbol(value)
        assert MarketPriceUnit.symbol_to_value(symbol) == value
