"""Tests for schema enum market.type.name.000"""

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
