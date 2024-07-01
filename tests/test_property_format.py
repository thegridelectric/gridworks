from typing import Any

import pytest
from pydantic import BaseModel
from pydantic import ValidationError

import gw
from gw.property_format import predicate_validator


def test_property_format():
    assert gw.property_format.is_bit(0)
    assert gw.property_format.is_bit(1)
    assert not gw.property_format.is_bit(2)

    assert gw.property_format.is_64_bit_hex("12345abc")
    assert not gw.property_format.is_64_bit_hex("12345abcd")
    assert not gw.property_format.is_64_bit_hex("1234567g")

    # noinspection PyTypeChecker
    assert not gw.property_format.is_left_right_dot(5)
    assert not gw.property_format.is_left_right_dot("5.a-h")
    assert gw.property_format.is_left_right_dot("a.s")

    assert gw.property_format.is_unsigned_short(0)
    assert gw.property_format.is_unsigned_short(65535)
    assert not gw.property_format.is_unsigned_short(65536)
    assert not gw.property_format.is_unsigned_short(-1)

    assert gw.property_format.is_short_integer(-32768)
    assert gw.property_format.is_short_integer(32767)
    assert not gw.property_format.is_short_integer(-32769)
    assert not gw.property_format.is_short_integer(32768)

    good_market_name = "rt60gate5.d1.isone"
    bad_market_name_1 = "not_a_market_type.d1.isone"
    bad_market_name_2 = "rt60gate5.d1.not-lrd"

    gw.property_format.check_is_market_name(good_market_name)

    with pytest.raises(ValueError):
        gw.property_format.check_is_market_name(bad_market_name_1)

    with pytest.raises(ValueError):
        gw.property_format.check_is_market_name(bad_market_name_2)

    good_market_slot_name = "rt60gate5.d1.isone.ver.keene.1673539200"
    bad_market_slot_name_1 = bad_market_name_1 + ".1673539200"
    bad_slot_start_1 = "rt60gate5.d1.isone.ver.keene.not_unix_s"
    bad_slot_start_2 = "rt60gate5.d1.isone.ver.keene.777"
    bad_slot_start_3 = "rt60gate5.d1.isone.ver.keene.1673539205"

    gw.property_format.check_is_market_slot_name_lrd_format(good_market_slot_name)
    with pytest.raises(ValueError):
        gw.property_format.check_is_market_slot_name_lrd_format(bad_market_slot_name_1)

    with pytest.raises(ValueError):
        gw.property_format.check_is_market_slot_name_lrd_format(bad_slot_start_1)

    with pytest.raises(ValueError):
        gw.property_format.check_is_market_slot_name_lrd_format(bad_slot_start_2)
    with pytest.raises(ValueError):
        gw.property_format.check_is_market_slot_name_lrd_format(bad_slot_start_3)


def test_predicate_validator():
    def is_truthy(v: Any) -> bool:
        return bool(v)

    class Foo(BaseModel):
        an_int: int
        some_ints: list[int]
        list_with_contents: list
        _validate_an_int = predicate_validator("an_int", is_truthy)
        _validate_some_ints = predicate_validator(
            "some_ints", is_truthy, each_item=True
        )
        _validate_list_with_contents = predicate_validator(
            "list_with_contents", is_truthy
        )

    # predicates pass
    Foo(an_int=1, some_ints=[1, 2, 3], list_with_contents=[False, "xyz"])
    Foo(an_int=1, some_ints=[1, "2", 3], list_with_contents=[False, "xyz"])
    Foo(an_int=1, some_ints=[], list_with_contents=[False, "xyz"])

    # predicates pass with implicit type conversion
    # noinspection PyTypeChecker
    Foo(an_int="45", some_ints=[1, 2, 3], list_with_contents=[False])

    # scalar field validation
    with pytest.raises(ValidationError):
        Foo(an_int=0, some_ints=[1, 2, 3], list_with_contents=[False])

    # field type annotation still used
    with pytest.raises(ValidationError):
        # noinspection PyTypeChecker
        Foo(an_int="yes!", some_ints=[1, 2, 3], list_with_contents=[False])

    # field type annotation still used - convertible value ok.
    with pytest.raises(ValidationError):
        Foo(an_int=False, some_ints=[1, 2, 3], list_with_contents=[False])

    # field type annotation still used.
    with pytest.raises(ValidationError):
        # noinspection PyTypeChecker
        Foo(an_int="0", some_ints=[1, 2, 3], list_with_contents=[False])

    # per_item validator applied as expected
    with pytest.raises(ValidationError):
        Foo(an_int=1, some_ints=[1, 2, 3, "z"], list_with_contents=[False, "xyz"])

    # non-per_item validator on list
    with pytest.raises(ValidationError):
        Foo(an_int=1, some_ints=[1, 2, 3], list_with_contents=[])
