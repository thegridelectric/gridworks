from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class UniverseType(StrEnum):
    Dev = auto()
    Hybrid = auto()

    @classmethod
    def default(cls) -> "UniverseType":
        return cls.Dev

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
