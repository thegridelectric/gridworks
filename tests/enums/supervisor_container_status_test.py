"""Tests for schema enum supervisor.container.status.000"""
from gridworks.enums import SupervisorContainerStatus


def test_supervisor_container_status() -> None:
    assert set(SupervisorContainerStatus.values()) == {
        "Unknown",
        "Authorized",
        "Launching",
        "Provisioning",
        "Running",
        "Stopped",
        "Deleted",
    }

    assert SupervisorContainerStatus.default() == SupervisorContainerStatus.Unknown
