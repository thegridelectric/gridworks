from typing import List

from gw.data_classes.market_type import MarketType
from gw.enums import MarketTypeName


def check_is_market_name(v: str) -> None:
    try:
        x = v.split(".")
    except AttributeError:
        raise ValueError(f"{v} failed to split on '.'")
    if not x[0] in MarketTypeName.values():
        raise ValueError(f"{v} not recognized MarketType")
    g_node_alias = ".".join(x[1:])
    check_is_left_right_dot(g_node_alias)


def check_is_market_slot_name_lrd_format(v: str) -> None:
    """
    MaketSlotNameLrdFormat: the format of a MarketSlotName.
      - The first word must be a MarketTypeName
      - The last word (unix time of market slot start) must
      be a 10-digit integer divisible by 300 (i.e. all MarketSlots
      start at the top of 5 minutes)
      - More strictly, the last word must be the start of a
      MarketSlot for that MarketType (i.e. divisible by 3600
      for hourly markets)
      - The middle words have LeftRightDot format (GNodeAlias
      of the MarketMaker)
    Example: rt60gate5.d1.isone.ver.keene.1673539200

    """
    try:
        x = v.split(".")
    except AttributeError:
        raise ValueError(f"{v} failed to split on '.'")
    slot_start = x[-1]
    try:
        slot_start = int(slot_start)
    except ValueError:
        raise ValueError(f"slot start {slot_start} not an int")
    check_is_reasonable_unix_time_s(slot_start)
    if slot_start % 300 != 0:
        raise ValueError(f"slot start {slot_start} not a multiple of 300")

    market_name = ".".join(x[:-1])
    try:
        check_is_market_name(market_name)
    except ValueError as e:
        raise ValueError(f"e")
    market_type = MarketType.by_id[MarketTypeName(x[0])]
    if not slot_start % (market_type.duration_minutes * 60) == 0:
        raise ValueError(
            f"market_slot_start_s mod {(market_type.duration_minutes * 60)} must be 0"
        )


def check_is_left_right_dot(candidate: str) -> None:
    """Lowercase AlphanumericStrings separated by dots (i.e. periods), with most
    significant word to the left.  I.e. `d1.ne` is the child of `d1`.
    Checking the format cannot verify the significance of words. All
    words must be alphanumeric. Most significant word must start with
    an alphabet charecter


    Raises:
        ValueError: if candidate is not of lrd format (e.g. d1.iso.me.apple)
    """
    try:
        x: List[str] = candidate.split(".")
    except:
        raise ValueError("Failed to seperate into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word must start with alphabet char. Got '{first_word}'"
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(
                f"words seperated by dots must be alphanumeric. Got '{word}'"
            )
    if not candidate.islower():
        raise ValueError(f"alias must be lowercase. Got '{candidate}'")


def check_is_reasonable_unix_time_s(v: int) -> None:
    """
    ReasonableUnixTimeS format: time in unix seconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeS format
    """
    from datetime import datetime
    from datetime import timezone

    start_date = datetime(2000, 1, 1, tzinfo=timezone.utc)
    end_date = datetime(3000, 1, 1, tzinfo=timezone.utc)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    if v < start_timestamp:
        raise ValueError(f"{v} must be after Jan 1 2000")
    if v > end_timestamp:
        raise ValueError(f"{v} must be before Jan 1 3000")
