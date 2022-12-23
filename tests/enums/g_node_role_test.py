"""Tests for schema enum g.node.role.000"""
from gridworks.enums import GNodeRole


def test_g_node_role() -> None:
    assert set(GNodeRole.values()) == {
        "Unknown",
        "TerminalAsset",
        "Scada",
        "PriceService",
        "WeatherService",
        "AtomicMeteringNode",
        "AtomicTNode",
        "MarketMaker",
        "ConductorTopologyNode",
        "InterconnectionComponent",
        "World",
        "TimeCoordinator",
        "Supervisor",
    }

    assert GNodeRole.default() == GNodeRole.Unknown
