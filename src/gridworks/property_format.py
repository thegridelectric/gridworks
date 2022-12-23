import string
import struct
from typing import Any
from typing import Callable
from typing import List

import algosdk  # type: ignore[import]
import algosdk.abi  # type: ignore[import]
import pendulum
import pydantic


def predicate_validator(
    field_name: str, predicate: Callable[[Any], bool], error_format: str = ""
) -> classmethod:  # type: ignore
    def _validator(v: Any) -> Any:
        if not predicate(v):
            if error_format:
                err_str = error_format.format(value=v)
            else:
                err_str = f"{field_name}: {predicate} fails for [{v}]"
            raise ValueError(err_str)
        return v

    return pydantic.validator(field_name, allow_reuse=True)(_validator)


def is_algo_address_string_format(candidate: str) -> bool:
    """The public key of a private/public Ed25519 key pairis transformed into an Algorand address,
    by adding a 4-byte checksum to the end of the public key and then encoding it
    in base32.

    Args:
        candidate (str): candidate

    Returns:
        bool: True if is_algo_address_string_format
    """

    at = algosdk.abi.AddressType()
    try:
        result = at.decode(at.encode(candidate))
    except Exception as e:
        return False
    return True


def check_is_algo_address_string_format(candidate: str) -> None:
    """Note: could use algosdk.encoding.is_valid_address instead.
    Leaving in for the moment to keep looking at algosdk.abi and understand
    how to use it.

    The public key of a private/public Ed25519 key pairis transformed into an Algorand address,
    by adding a 4-byte checksum to the end of the public key and then encoding it
    in base32.

    Args:
        candidate (str): candidate

    Raises:
        ValueError: Throw ValueError if algorand AddressType decode(encode(c)) fails.
    """

    at = algosdk.abi.AddressType()
    try:
        result = at.decode(at.encode(candidate))
    except Exception as e:
        raise ValueError(f"Not AlgoAddressStringFormat: {e}")


def is_algo_private_key_format(candidate: str) -> bool:
    """The private key of a private/public Ed25519 key pair is transformed into an Algorand address,
    by adding a 4-byte checksum to the end of the public key and then encoding it
    in base32

    Args:
        candidate (str): _description_

    Returns:
        bool: True if candidate is_alg_private_key_format
    """
    try:
        algosdk.account.address_from_private_key(candidate)
    except Exception as e:
        return False
    return True


def check_is_algo_private_key_format(candidate: str) -> None:
    """The private key of a private/public Ed25519 key pair is transformed into an Algorand address,
    by adding a 4-byte checksum to the end of the public key and then encoding it
    in base32

    Args:
        candidate (str): candidate

    Raises:
        ValueError: if not is_algo_private_key_foramt
    """
    try:
        algosdk.account.address_from_private_key(candidate)
    except Exception as e:
        raise ValueError(f"Not AlgoSecretKeyFormat: {e} /n {candidate} ")


def is_algo_msg_pack_encoded(candidate: str) -> bool:
    try:
        algosdk.encoding.future_msgpack_decode(candidate)
    except Exception as e:
        return False
    return True


def check_is_algo_msg_pack_encoded(candidate: str) -> None:
    try:
        algosdk.encoding.future_msgpack_decode(candidate)
    except Exception as e:
        raise ValueError(f"Not AlgoMsgPackEncoded: {e} /n {candidate}")


def is_valid_asa_name(candidate: str) -> bool:
    """a string no more than 32 chars

    Args:
        candidate (str): candidate

    Returns:
        bool: True if a string no more than 32 cars
    """
    try:
        l = len(candidate)
    except Exception as e:
        return False
    if l > 32:
        return False
    return True


def check_is_valid_asa_name(candidate: str) -> None:
    try:
        l = len(candidate)
    except Exception as e:
        raise ValueError(f"Not ValidAsaName: {e} /n {candidate} ")
    if l > 32:
        raise ValueError(
            f"Not ValidAsaName: AsaNames must be <= 32 /n {candidate} is {len(candidate)}"
        )


def is_64_bit_hex(candidate: str) -> bool:
    if len(candidate) != 8:
        return False
    if not all(c in string.hexdigits for c in candidate):
        return False
    return True


def check_is_64_bit_hex(candidate: str) -> None:
    if len(candidate) != 8:
        raise ValueError(f" {candidate} Must be length 8, not {len(candidate)}")
    if not all(c in string.hexdigits for c in candidate):
        raise ValueError("Must be hex digits")


def is_bit(candidate: int) -> bool:
    if candidate not in {0, 1}:
        return False
    return True


def check_is_bit(candidate: int) -> None:
    if candidate not in {0, 1}:
        raise ValueError(f"{candidate} must be either 0 or 1")


def is_lrd_alias_format(candidate: str) -> bool:
    """Lowercase AlphanumericStrings separated by dots (i.e. periods), with most
    significant word to the left.  I.e. `d1.ne` is the child of `d1`.
    Checking the format cannot verify the significance of words. All
    words must be alphanumeric. Most significant word must start with
    an alphabet charecter

    Args:
        candidate (str): candidate

    Returns:
        bool: True if is_lrod_alias_format
    """
    try:
        x = candidate.split(".")
    except:
        return False
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        return False
    for word in x:
        if not word.isalnum():
            return False
    if not candidate.islower():
        return False
    return True


def check_is_lrd_alias_format(candidate: str) -> None:
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


def is_lru_alias_format(candidate: str) -> bool:
    """AlphanumericStrings separated by underscores, with most
    significant word to the left.  I.e. `d1.ne` is the child of `d1`.
    Checking the format cannot verify the significance of words. All
    words must be alphanumeric. Most significant word must start with
    an alphabet charecter"""
    try:
        x = candidate.split("_")
    except:
        return False
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        return False
    for word in x:
        if not word.isalnum():
            return False
    if not candidate.islower():
        return False
    return True


def is_lrh_alias_format(candidate: str) -> bool:
    """AlphanumericStrings separated by hyphens, with most
    significant word to the left.  I.e. `d1.ne` is the child of `d1`.
    Checking the format cannot verify the significance of words. All
    words must be alphanumeric. Most significant word must start with
    an alphabet charecter"""
    try:
        x = candidate.split("-")
    except:
        return False
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        return False
    for word in x:
        if not word.isalnum():
            return False
    if not candidate.islower():
        return False
    return True


def is_positive_integer(candidate: int) -> bool:
    if not isinstance(candidate, int):
        return False  # type: ignore[unreachable]
    if candidate <= 0:
        return False
    return True


def check_is_positive_integer(candidate: int) -> None:
    if not isinstance(candidate, int):
        raise ValueError("Must be an integer")
    if candidate <= 0:
        raise ValueError("Must be positive integer")


def is_reasonable_unix_time_ms(candidate: int) -> bool:
    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > candidate:  # type: ignore[attr-defined]
        return False
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < candidate:  # type: ignore[attr-defined]
        return False
    return True


def check_is_reasonable_unix_time_ms(candidate: int) -> None:
    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > candidate:  # type: ignore[attr-defined]
        raise ValueError("ReasonableUnixTimeMs must be after 2000 AD")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < candidate:  # type: ignore[attr-defined]
        raise ValueError("ReasonableUnixTimeMs must be before 3000 AD")


def is_reasonable_unix_time_s(candidate: int) -> bool:
    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp > candidate:  # type: ignore[attr-defined]
        return False
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp < candidate:  # type: ignore[attr-defined]
        return False
    return True


def check_is_reasonable_unix_time_s(candidate: int) -> None:
    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp > candidate:  # type: ignore[attr-defined]
        raise ValueError("ReasonableUnixTimeS must be after 2000 AD")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp < candidate:  # type: ignore[attr-defined]
        raise ValueError("ReasonableUnixTimeS must be before 3000 AD")


def is_unsigned_short(candidate: int) -> bool:
    try:
        struct.pack("H", candidate)
    except:
        return False
    return True


def check_is_unsigned_short(candidate: int) -> None:
    try:
        struct.pack("H", candidate)
    except:
        raise ValueError("requires 0 <= number <= 65535")


def is_short_integer(candidate: int) -> bool:
    try:
        struct.pack("h", candidate)
    except:
        return False
    return True


def check_is_short_integer(candidate: int) -> None:
    try:
        struct.pack("h", candidate)
    except:
        raise ValueError("short format requires (-32767 -1) <= number <= 32767")


def is_uuid_canonical_textual(candidate: str) -> bool:
    try:
        x = candidate.split("-")
    except AttributeError:
        return False
    if len(x) != 5:
        return False
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            return False
    if len(x[0]) != 8:
        return False
    if len(x[1]) != 4:
        return False
    if len(x[2]) != 4:
        return False
    if len(x[3]) != 4:
        return False
    if len(x[4]) != 12:
        return False
    return True


def check_is_uuid_canonical_textual(candidate: str) -> None:
    try:
        x = candidate.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"Did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError("Words are not all hex")
    if len(x[0]) != 8:
        raise ValueError("Word 0  not of length 8")
    if len(x[1]) != 4:
        raise ValueError("Word 1 not of length 4")
    if len(x[2]) != 4:
        raise ValueError("Word 2 not of length 4")
    if len(x[3]) != 4:
        raise ValueError("Word 3 not of length 4")
    if len(x[4]) != 12:
        raise ValueError("Word 4 not of length 12")


def check_world_alias_matches_universe(g_node_alias: str, universe: str) -> None:
    """
    Raises:
        ValueError: if g_node_alias is not LRD format or if first word does not match universe
    """
    check_is_lrd_alias_format(g_node_alias)
    world_alias = g_node_alias.split(".")[0]
    if universe == "dev":
        if world_alias[0] != "d":
            raise ValueError(
                f"World alias for dev universe must start with d. Got {world_alias}"
            )


def is_world_instance_alias_format(candidate: str) -> bool:
    try:
        words = candidate.split("__")
    except:
        return False
    try:
        int(words[1])
    except:
        return False
    try:
        alias_words = words[0].split(".")
    except:
        return False
    if len(alias_words) > 1:
        return False
    return True
