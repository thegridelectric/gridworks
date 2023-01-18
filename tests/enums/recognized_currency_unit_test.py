"""Tests for schema enum recognized.currency.unit.000"""
from gridworks.enums import RecognizedCurrencyUnit


def test_recognized_currency_unit() -> None:
    assert set(RecognizedCurrencyUnit.values()) == {
        "UNKNOWN",
        "USD",
        "GBP",
    }

    assert RecognizedCurrencyUnit.default() == RecognizedCurrencyUnit.UNKNOWN
