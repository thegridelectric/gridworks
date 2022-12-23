"""Tests for schema enum strategy.name.000"""
from gridworks.enums import StrategyName


def test_strategy_name() -> None:
    assert set(StrategyName.values()) == {
        "NoActor",
        "WorldA",
        "SupervisorA",
        "AtnHeatPumpWithBoostStore",
        "TcGlobalA",
        "MarketMakerA",
    }

    assert StrategyName.default() == StrategyName.NoActor
