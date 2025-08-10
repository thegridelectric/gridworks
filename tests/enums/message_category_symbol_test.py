"""
Tests for enum message.category.symbol.000 from the GridWorks Type Registry.
"""

from gw.enums import MessageCategorySymbol


def test_message_category_symbol() -> None:
    assert set(MessageCategorySymbol.values()) == {
        "unknown",
        "rj",
        "rjb",
        "gw",
        "s",
    }

    assert MessageCategorySymbol.default() == MessageCategorySymbol.unknown
    assert MessageCategorySymbol.enum_name() == "message.category.symbol"
    assert MessageCategorySymbol.enum_version() == "000"

