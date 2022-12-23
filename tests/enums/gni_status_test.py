"""Tests for schema enum gni.status.000"""
from gridworks.enums import GniStatus


def test_gni_status() -> None:
    assert set(GniStatus.values()) == {
        "Unknown",
        "Pending",
        "Active",
        "Done",
    }

    assert GniStatus.default() == GniStatus.Unknown
