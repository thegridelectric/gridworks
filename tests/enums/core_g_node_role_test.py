"""Tests for schema enum core.g.node.role.000"""
from gridworks.enums import CoreGNodeRole


def test_core_g_node_role() -> None:
    assert set(CoreGNodeRole.values()) == {
        "Other",
        "TerminalAsset",
        "AtomicTNode",
        "MarketMaker",
        "AtomicMeteringNode",
        "ConductorTopologyNode",
        "InterconnectionComponent",
        "Scada",
    }

    assert CoreGNodeRole.default() == CoreGNodeRole.Other
