from enum import auto
from typing import List

from gridworks.enums import GwStrEnum


class StrategyName(GwStrEnum):
    """
    Used to assign code to run a particular GNodeInstance

    Choices and descriptions:

      * NoActor: Assigned to GNodes that do not have actors
      * WorldA: Authority on GNodeInstances, and their private keys. Maintains a FastAPI used for relational information about backoffice information held locally and/or in the GNodeRegistry/GNodeFactory. [More Info](https://gridworks.readthedocs.io/en/latest/world-role.html)
      * SupervisorA: A simple supervisor that monitors its supervised AtomicTNode GNode strategies via a heartbeat health check. [More Info](https://gridworks.readthedocs.io/en/latest/supervisor.html)
      * AtnHeatPumpWithBoostStore: AtomicTNode for a heat pump thermal storage heating system with a boost element and a thermal \n heated by the boost element. [More on AtomicTNodes](https://gridworks.readthedocs.io/en/latest/atomic-t-node.html)
      * TcGlobalA: Used to manage the global time of the Gridworks system when run with\n in a fully simulated universe. \n [More on TimeCoordinators](https://gridworks.readthedocs.io/en/latest/time-coordinator.html)
      * MarketMakerA: Runs a two-sided market associated to its GNode as part of the copper GNode sub-tree. [More on MarketMakers](https://gridworks.readthedocs.io/en/latest/market-maker.html)
      * AtnBrickStorageHeater: Publicly available Dijkstra-based AtomicTNode strategy for a brick storage heater. These heaters are rooom units that store heat in a brick core, are heated with resistive elements, and typically have a fan to blow air over the brick core. They are sometimes called Electric Thermal Storage (ETS) heaters, and in the UK are often called Economy 7 heaters or Night Storage Heaters. A strategy very similar to this was used by VCharge to manage an ETS fleet of several thousand heaters in Pennsylvania. This strategy is meant to serve as a template for other private strategies, and also allows for an end-to-end simulation of a realistic aggregated transactive load capable of generating a highly elastic bid curve [More Info](https://gridworks-atn.readthedocs.io/en/latest/brick-storage-heater.html)
    """

    NoActor = auto()
    WorldA = auto()
    SupervisorA = auto()
    AtnHeatPumpWithBoostStore = auto()
    TcGlobalA = auto()
    MarketMakerA = auto()
    AtnBrickStorageHeater = auto()

    @classmethod
    def default(cls) -> "StrategyName":
        """
        Returns default value NoActor
        """
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
