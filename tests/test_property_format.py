import pytest

from gw import check_is_market_name
from gw import check_is_market_slot_name_lrd_format


def test_property_format() -> None:

    good_market_name = "rt60gate5.d1.isone"
    bad_market_name_1 = "not_a_market_type.d1.isone"
    bad_market_name_2 = "rt60gate5.d1.not-lrd"

    check_is_market_name(good_market_name)

    with pytest.raises(ValueError):
        check_is_market_name(bad_market_name_1)

    with pytest.raises(ValueError):
        check_is_market_name(bad_market_name_2)

    good_market_slot_name = "rt60gate5.d1.isone.ver.keene.1673539200"
    bad_market_slot_name_1 = bad_market_name_1 + ".1673539200"
    bad_slot_start_1 = "rt60gate5.d1.isone.ver.keene.not_unix_s"
    bad_slot_start_2 = "rt60gate5.d1.isone.ver.keene.777"
    bad_slot_start_3 = "rt60gate5.d1.isone.ver.keene.1673539205"

    check_is_market_slot_name_lrd_format(good_market_slot_name)
    with pytest.raises(ValueError):
        check_is_market_slot_name_lrd_format(bad_market_slot_name_1)

    with pytest.raises(ValueError):
        check_is_market_slot_name_lrd_format(bad_slot_start_1)

    with pytest.raises(ValueError):
        check_is_market_slot_name_lrd_format(bad_slot_start_2)

    with pytest.raises(ValueError):
        check_is_market_slot_name_lrd_format(bad_slot_start_3)
