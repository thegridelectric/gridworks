"""Tests for schema enum universe.type.000"""
from gridworks.enums import UniverseType


def test_universe_type() -> None:
    assert set(UniverseType.values()) == {
        "Dev",
        "Hybrid",
    }

    assert UniverseType.default() == UniverseType.Dev
