from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class SupervisorContainerStatus(StrEnum):
    Unknown = auto()
    Authorized = auto()
    Launching = auto()
    Provisioning = auto()
    Running = auto()
    Stopped = auto()
    Deleted = auto()

    @classmethod
    def default(cls) -> "SupervisorContainerStatus":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
