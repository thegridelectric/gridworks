from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class GNodeRole(StrEnum):
    """
    Categorizes GNodes by their function within GridWorks. [More Info](https://gridworks.readthedocs.io/en/latest/g-node-role.html).

    Choices and descriptions:

      * GNode: Default value
      * TerminalAsset: An avatar for a real-word Transactive Device. [More Info](https://gridworks.readthedocs.io/en/latest/transactive-device.html).
      * AtomicTNode: Transacts in markets on behalf of, and controlling the power use of, a TerminalAsset
      * MarketMaker: Runs energy markets at its Node in the GNodeTree
      * AtomicMeteringNode: Role of a GNode that will become an AtomicTNode, prior to it owning TaTradingRights
      * ConductorTopologyNode: An avatar for a real-world electric grid node - e.g. a substation or transformer
      * InterconnectionComponent: An avatar for a cable or wire on the electric grid
      * World: Adminstrative GNode responsible for managing and authorizing instances
      * TimeCoordinator: Responsible for managing time in simulations
      * Supervisor: Responsible for GNode actors running in a container
      * Scada: GNode associated to the device and code that directly monitors and actuates a Transactive Device
      * PriceService: Provides price forecasts for markets run by MarketMakers
      * WeatherService: Provides weather forecasts
      * AggregatedTNode: An aggregation of AtomicTNodes
      * Persister: Responsible for acking events with delivery guarantees
    """

    GNode = auto()
    TerminalAsset = auto()
    Scada = auto()
    PriceService = auto()
    WeatherService = auto()
    AggregatedTNode = auto()
    Persister = auto()
    AtomicTNode = auto()
    MarketMaker = auto()
    AtomicMeteringNode = auto()
    ConductorTopologyNode = auto()
    InterconnectionComponent = auto()
    World = auto()
    TimeCoordinator = auto()
    Supervisor = auto()

    @classmethod
    def default(cls) -> "GNodeRole":
        """
        Returns default value GNode
        """
        return cls.GNode

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
