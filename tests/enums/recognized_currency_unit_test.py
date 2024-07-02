"""
Tests for enum recognized.currency.unit.000 from the GridWorks Type Registry.
"""

from gw.enums import RecognizedCurrencyUnit


def test_recognized_currency_unit() -> None:
    assert set(RecognizedCurrencyUnit.values()) == {
        "UNKNOWN",
        "USD",
        "GBP",
    }

    assert RecognizedCurrencyUnit.default() == RecognizedCurrencyUnit.UNKNOWN
    assert RecognizedCurrencyUnit.enum_name() == "recognized.currency.unit"
    assert RecognizedCurrencyUnit.enum_version() == "000"

    assert RecognizedCurrencyUnit.version("UNKNOWN") == "000"
    assert RecognizedCurrencyUnit.version("USD") == "000"
    assert RecognizedCurrencyUnit.version("GBP") == "000"

    for value in RecognizedCurrencyUnit.values():
        symbol = RecognizedCurrencyUnit.value_to_symbol(value)
        assert RecognizedCurrencyUnit.symbol_to_value(symbol) == value
