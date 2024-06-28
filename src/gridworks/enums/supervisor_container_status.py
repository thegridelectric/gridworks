from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class SupervisorContainerStatus(GwStrEnum):
    """
    Manages lifecycle of the docker containers where GridWorks actors run

    Choices and descriptions:

      * Unknown: Default value
      * Authorized: World has created the information for starting the container
      * Launching: World has launched the container
      * Provisioning: Container has started, but is going through its provisioning process
      * Running: GNode actors in the container are active
      * Stopped: Stopped
      * Deleted: Deleted
    """

    Unknown = auto()
    Authorized = auto()
    Launching = auto()
    Provisioning = auto()
    Running = auto()
    Stopped = auto()
    Deleted = auto()

    @classmethod
    def default(cls) -> "SupervisorContainerStatus":
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
