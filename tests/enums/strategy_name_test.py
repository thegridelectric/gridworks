"""Tests for schema enum strategy.name.001"""
from gridworks.enums import StrategyName


def test_strategy_name() -> None:
    assert set(StrategyName.values()) == {
        "NoActor",
        "WorldA",
        "SupervisorA",
        "AtnHeatPumpWithBoostStore",
        "TcGlobalA",
        "MarketMakerA",
        "AtnBrickStorageHeater",
    }

    assert StrategyName.default() == StrategyName.NoActor
