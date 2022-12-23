from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MessageCategorySymbol(StrEnum):
    unknown = auto()
    rj = auto()
    rjb = auto()
    s = auto()
    gw = auto()
    post = auto()
    postack = auto()
    get = auto()

    @classmethod
    def default(cls) -> "MessageCategorySymbol":
        return cls.unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]
