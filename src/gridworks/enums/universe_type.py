from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class UniverseType(StrEnum):
    """
    Allows for multiple GridWorks, in particular for development and shared simulations. [More Info](https://gridworks.readthedocs.io/en/latest/universe.html).

    Choices and descriptions:

      * Dev: Simulation running on a single computer.
      * Hybrid: Anything goes.
      * Production: Money at stake.
    """

    Dev = auto()
    Hybrid = auto()
    Production = auto()

    @classmethod
    def default(cls) -> "UniverseType":
        """
        Returns default value Dev
        """
        return cls.Dev

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
