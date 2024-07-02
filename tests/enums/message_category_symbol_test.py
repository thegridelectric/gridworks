"""
Tests for enum message.category.symbol.000 from the GridWorks Type Registry.
"""

from gw.enums import MessageCategorySymbol


def test_message_category_symbol() -> None:
    assert set(MessageCategorySymbol.values()) == {
        "unknown",
        "rj",
        "rjb",
        "s",
        "gw",
        "post",
        "postack",
        "get",
    }

    assert MessageCategorySymbol.default() == MessageCategorySymbol.unknown
    assert MessageCategorySymbol.enum_name() == "message.category.symbol"
    assert MessageCategorySymbol.enum_version() == "000"

    assert MessageCategorySymbol.version("unknown") == "000"
    assert MessageCategorySymbol.version("rj") == "000"
    assert MessageCategorySymbol.version("rjb") == "000"
    assert MessageCategorySymbol.version("s") == "000"
    assert MessageCategorySymbol.version("gw") == "000"
    assert MessageCategorySymbol.version("post") == "000"
    assert MessageCategorySymbol.version("postack") == "000"
    assert MessageCategorySymbol.version("get") == "000"

    for value in MessageCategorySymbol.values():
        symbol = MessageCategorySymbol.value_to_symbol(value)
        assert MessageCategorySymbol.symbol_to_value(symbol) == value
