from typing import Dict

from pydantic import BaseModel

from gridworks.enums import MarketPriceUnit
from gridworks.enums import MarketQuantityUnit
from gridworks.enums import MarketTypeName
from gridworks.enums import RecognizedCurrencyUnit


class MarketType:
    by_id: Dict[MarketTypeName, "MarketType"] = {}

    def __new__(cls, name: MarketTypeName, *args, **kwargs) -> "MarketType":  # type: ignore
        try:
            return cls.by_id[name]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[name] = instance
            return instance

    def __init__(
        self,
        name: MarketTypeName,
        duration_minutes: int,
        gate_closing_seconds: int,
        price_max: int,
        price_unit: MarketPriceUnit = MarketPriceUnit.USDPerMWh,
        quantity_unit: MarketQuantityUnit = MarketQuantityUnit.AvgMW,
        currency_unit: RecognizedCurrencyUnit = RecognizedCurrencyUnit.USD,
    ):
        self.name = name
        self.duration_minutes = duration_minutes
        self.gate_closing_seconds = gate_closing_seconds
        self.price_max = price_max
        self.price_unit = price_unit
        self.quantity_unit = quantity_unit
        self.currency_unit = currency_unit

    def __repr__(self) -> str:
        s = f"MarketType {self.name}: duration {self.duration_minutes} m, gate closing {self.gate_closing_seconds} s, {self.price_unit.value}, {self.quantity_unit.value}"
        return s


Rt5Gate5 = MarketType(
    name=MarketTypeName.rt5gate5,
    duration_minutes=5,
    gate_closing_seconds=5 * 60,
    price_max=10_000,
)

Rt15Gate5 = MarketType(
    name=MarketTypeName.rt15gate5,
    duration_minutes=15,
    gate_closing_seconds=5 * 60,
    price_max=10_000,
)

Rt30Gate5 = MarketType(
    name=MarketTypeName.rt30gate5,
    duration_minutes=30,
    gate_closing_seconds=5 * 60,
    price_max=10_000,
)

Rt60Gate5 = MarketType(
    name=MarketTypeName.rt60gate5,
    duration_minutes=60,
    gate_closing_seconds=5 * 60,
    price_max=10_000,
)

Rt60Gate30 = MarketType(
    name=MarketTypeName.rt60gate30,
    duration_minutes=60,
    gate_closing_seconds=30 * 60,
    price_max=10_000,
)

Rt60Gate30B = MarketType(
    name=MarketTypeName.rt60gate30b,
    duration_minutes=60,
    gate_closing_seconds=60,
    price_max=10_000,
    quantity_unit=MarketQuantityUnit.AvgkW,
)

Da60 = MarketType(
    name=MarketTypeName.da60,
    duration_minutes=60,
    gate_closing_seconds=1440,
    price_max=10_000,
)
