import uuid
from typing import Any

import pendulum
import pytest
from pydantic import BaseModel
from pydantic import ValidationError

import gridworks
from gridworks.property_format import predicate_validator


def test_property_format():
    assert gridworks.property_format.is_bit(0)
    assert gridworks.property_format.is_bit(1)
    assert not gridworks.property_format.is_bit(2)

    assert gridworks.property_format.is_64_bit_hex("12345abc")
    assert not gridworks.property_format.is_64_bit_hex("12345abcd")
    assert not gridworks.property_format.is_64_bit_hex("1234567g")

    # noinspection PyTypeChecker
    assert not gridworks.property_format.is_left_right_dot(5)
    assert not gridworks.property_format.is_left_right_dot("5.a-h")
    assert gridworks.property_format.is_left_right_dot("a.s")

    bad_date_1 = pendulum.datetime(year=3000, month=1, day=1, hour=1)
    bad_date_2 = pendulum.datetime(year=1999, month=12, day=31, hour=23)
    good_date = pendulum.datetime(year=2200, month=1, day=1, hour=1)

    assert not gridworks.property_format.is_reasonable_unix_time_ms(
        int(bad_date_1.timestamp() * 1000)
    )
    assert not gridworks.property_format.is_reasonable_unix_time_ms(
        int(bad_date_2.timestamp() * 1000)
    )
    assert not gridworks.property_format.is_reasonable_unix_time_ms(
        int(good_date.timestamp())
    )
    assert gridworks.property_format.is_reasonable_unix_time_ms(
        int(good_date.timestamp() * 1000)
    )

    assert gridworks.property_format.is_reasonable_unix_time_s(
        int(good_date.timestamp())
    )
    assert not gridworks.property_format.is_reasonable_unix_time_s(
        int(good_date.timestamp() * 1000)
    )
    assert not gridworks.property_format.is_reasonable_unix_time_s(
        int(bad_date_1.timestamp())
    )
    assert not gridworks.property_format.is_reasonable_unix_time_s(
        int(bad_date_2.timestamp())
    )

    assert gridworks.property_format.is_unsigned_short(0)
    assert gridworks.property_format.is_unsigned_short(65535)
    assert not gridworks.property_format.is_unsigned_short(65536)
    assert not gridworks.property_format.is_unsigned_short(-1)

    assert gridworks.property_format.is_short_integer(-32768)
    assert gridworks.property_format.is_short_integer(32767)
    assert not gridworks.property_format.is_short_integer(-32769)
    assert not gridworks.property_format.is_short_integer(32768)

    s = "d4be12d5-33ba-4f1f-b9e5-2582fe41241d"
    assert gridworks.property_format.is_uuid_canonical_textual(s)
    # noinspection PyTypeChecker
    assert not gridworks.property_format.is_uuid_canonical_textual(uuid.uuid4())
    fail1 = "d4be12d5-33ba-4f1f-b9e5"
    assert not gridworks.property_format.is_uuid_canonical_textual(fail1)
    fail2 = "d4be12d-33ba-4f1f-b9e5-2582fe41241d"
    assert not gridworks.property_format.is_uuid_canonical_textual(fail2)
    fail3 = "k4be12d5-33ba-4f1f-b9e5-2582fe41241d"
    assert not gridworks.property_format.is_uuid_canonical_textual(fail3)
    fail4 = "d4be12d5-33a-4f1f-b9e5-2582fe41241d"
    assert not gridworks.property_format.is_uuid_canonical_textual(fail4)
    fail5 = "d4be12d5-33ba-4f1-b9e5-2582fe41241d"
    assert not gridworks.property_format.is_uuid_canonical_textual(fail5)
    fail6 = "d4be12d5-33ba-4f1f-b9e-2582fe41241d"
    assert not gridworks.property_format.is_uuid_canonical_textual(fail6)
    fail7 = "d4be12d5-33ba-4f1f-b9e5-2582fe41241"
    assert not gridworks.property_format.is_uuid_canonical_textual(fail7)

    good_market_name = "rt60gate5.d1.isone"
    bad_market_name_1 = "not_a_market_type.d1.isone"
    bad_market_name_2 = "rt60gate5.d1.not-lrd"

    gridworks.property_format.check_is_market_name(good_market_name)

    with pytest.raises(ValueError):
        gridworks.property_format.check_is_market_name(bad_market_name_1)

    with pytest.raises(ValueError):
        gridworks.property_format.check_is_market_name(bad_market_name_2)

    good_market_slot_name = "rt60gate5.d1.isone.ver.keene.1673539200"
    bad_market_slot_name_1 = bad_market_name_1 + ".1673539200"
    bad_slot_start_1 = "rt60gate5.d1.isone.ver.keene.not_unix_s"
    bad_slot_start_2 = "rt60gate5.d1.isone.ver.keene.777"
    bad_slot_start_3 = "rt60gate5.d1.isone.ver.keene.1673539205"

    gridworks.property_format.check_is_market_slot_name_lrd_format(
        good_market_slot_name
    )
    with pytest.raises(ValueError):
        gridworks.property_format.check_is_market_slot_name_lrd_format(
            bad_market_slot_name_1
        )

    with pytest.raises(ValueError):
        gridworks.property_format.check_is_market_slot_name_lrd_format(bad_slot_start_1)

    with pytest.raises(ValueError):
        gridworks.property_format.check_is_market_slot_name_lrd_format(bad_slot_start_2)
    with pytest.raises(ValueError):
        gridworks.property_format.check_is_market_slot_name_lrd_format(bad_slot_start_3)


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
