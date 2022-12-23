from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class GniStatus(StrEnum):
    Unknown = auto()
    Pending = auto()
    Active = auto()
    Done = auto()

    @classmethod
    def default(cls) -> "GniStatus":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
