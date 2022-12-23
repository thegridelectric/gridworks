from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class GNodeStatus(StrEnum):
    Unknown = auto()
    Pending = auto()
    Active = auto()
    PermanentlyDeactivated = auto()
    Suspended = auto()

    @classmethod
    def default(cls) -> "GNodeStatus":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
