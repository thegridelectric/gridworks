"""Tests for schema enum market.quantity.unit.000"""
from gridworks.enums import MarketQuantityUnit


def test_market_quantity_unit() -> None:
    assert set(MarketQuantityUnit.values()) == {
        "AvgMW",
        "AvgkW",
    }

    assert MarketQuantityUnit.default() == MarketQuantityUnit.AvgMW
