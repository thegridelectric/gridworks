import gw.utils
from gw.enums import MessageCategory
from gw.enums import MessageCategorySymbol


def test_pascal_camel() -> None:
    snake = "peaches_cat"
    camel = "PeachesCat"
    assert gw.utils.snake_to_pascal(snake) == camel
    assert gw.utils.pascal_to_snake(camel) == snake


def test_is_pascal() -> None:
    assert not gw.utils.is_pascal_case("not_pascal")
    assert not gw.utils.is_pascal_case("notPascal")
    assert gw.utils.is_pascal_case("IsPascal")


def test_message_category_from_symbol() -> None:
    """
    Bijection between shorthand and longhand enums
    """
    for s in MessageCategorySymbol:
        assert isinstance(s, MessageCategorySymbol)
        if s == MessageCategorySymbol.unknown:
            assert gw.utils.message_category_from_symbol(s) == MessageCategory.Unknown
        else:
            assert gw.utils.message_category_from_symbol(s) != MessageCategory.Unknown
