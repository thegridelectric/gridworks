"""Tests for schema enum market.price.unit.000"""

from gw.enums import MarketPriceUnit


def test_market_price_unit() -> None:
    assert set(MarketPriceUnit.values()) == {
        "USDPerMWh",
    }

    assert MarketPriceUnit.default() == MarketPriceUnit.USDPerMWh
