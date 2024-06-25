from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class GNodeStatus(GwStrEnum):
    """
    Enum for managing GNode lifecycle. [More Info](https://gridworks.readthedocs.io/en/latest/g-node-status.html).

    Choices and descriptions:

      * Unknown: Default value
      * Pending: The GNode exists but cannot be used yet.
      * Active: The GNode can be used.
      * PermanentlyDeactivated: The GNode can no longer be used, now or in the future.
      * Suspended: The GNode cannot be used, but may become active in the future.
    """

    Unknown = auto()
    Pending = auto()
    Active = auto()
    PermanentlyDeactivated = auto()
    Suspended = auto()

    @classmethod
    def default(cls) -> "GNodeStatus":
        """
        Returns default value Unknown
        """
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
