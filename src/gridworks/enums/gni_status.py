from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class GniStatus(GwStrEnum):
    """
    Enum for managing GNodeInstance lifecycle. [More Info](https://gridworks.readthedocs.io/en/latest/g-node-instance.html).

    Choices and descriptions:

      * Unknown: Default Value
      * Pending: Has been created by the World, but has not yet finished provisioning
      * Active: Active in its GridWorks world. If the GNodeInstance has an actor, that actor is communicating
      * Done: No longer represents the GNode.
    """

    Unknown = auto()
    Pending = auto()
    Active = auto()
    Done = auto()

    @classmethod
    def default(cls) -> "GniStatus":
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
