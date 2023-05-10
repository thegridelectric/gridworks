from typing import Dict
from typing import Optional

from gridworks.enums import GNodeRole
from gridworks.enums import StrategyName


class GNodeStrategy:
    by_id: Dict[StrategyName, "GNodeStrategy"] = {}

    def __new__(cls, name: StrategyName, *args, **kwargs) -> "GNodeStrategy":  # type: ignore
        try:
            return cls.by_id[name]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[name] = instance
            return instance

    def __init__(
        self,
        name: StrategyName,
        role: GNodeRole,
        contact_email: str,
        description: Optional[str] = "",
        is_private: bool = False,
        repo_url: Optional[str] = "None",
    ):
        self.name = name
        self.role = role
        self.contact_email = contact_email
        self.description = description
        self.is_private = is_private
        self.repo_url = repo_url

    def __repr__(self) -> str:
        s = (
            f"{self.role} GNodeStrategy {self.name.value}: Is Private: {self.is_private}, Repo: {self.repo_url}, contact: "
            f"{self.contact_email}\n {self.description}"
        )
        return s


NoActor = GNodeStrategy(
    name=StrategyName.NoActor,
    role=GNodeRole.GNode,
    contact_email="gridworks.gridworks-consulting.com",
    is_private=False,
    description="The NoActor strategy is a placeholder for a GNode that is passive and has no actor.",
)

SupervisorA = GNodeStrategy(
    name=StrategyName.SupervisorA,
    role=GNodeRole.Supervisor,
    contact_email="gridworks.gridworks-consulting.com",
    repo_url="https://github.com/thegridelectric/gridworks-atn",
    is_private=False,
    description="A simple supervisor that monitors its supervised AtomicTNode GNode strategies"
    "via a heartbeat health check. [More Info](https://gridworks.readthedocs.io/en/latest/supervisor.html)",
)

WorldA = GNodeStrategy(
    name=StrategyName.WorldA,
    role=GNodeRole.World,
    contact_email="gridworks.gridworks-consulting.com",
    repo_url="https://github.com/thegridelectric/gridworks-world",
    is_private=False,
    description="Authority on GNodeInstances, and their private keys. Maintains a FastAPI used "
    "for relational information about backoffice information held locally"
    "and/or in the GNodeRegistry/GNodeFactory. [More Info](https://gridworks.readthedocs.io/en/latest/world-role.html)",
)

AtnHeatPumpWithBoostStore = GNodeStrategy(
    name=StrategyName.AtnHeatPumpWithBoostStore,
    role=GNodeRole.AtomicTNode,
    contact_email="gridworks.gridworks-consulting.com",
    repo_url="https://github.com/thegridelectric/gridworks-atn-spaceheat",
    is_private=True,
    description="AtomicTNode for a heat pump thermal storage heating system with a boost element and a thermal "
    "heated by the boost element. "
    "[More on AtomicTNodes](https://gridworks.readthedocs.io/en/latest/atomic-t-node.html)",
)

TcGlobalA = GNodeStrategy(
    name=StrategyName.TcGlobalA,
    role=GNodeRole.TimeCoordinator,
    contact_email="gridworks.gridworks-consulting.com",
    repo_url="https://github.com/thegridelectric/gridworks-timecoordinator",
    is_private=False,
    description="Used to manage the global time of the Gridworks system when run with"
    "in a fully simulated universe. "
    "[More on TimeCoordinators](https://gridworks.readthedocs.io/en/latest/time-coordinator.html)",
)

MarketMakerA = GNodeStrategy(
    name=StrategyName.MarketMakerA,
    role=GNodeRole.MarketMaker,
    contact_email="gridworks.gridworks-consulting.com",
    repo_url="https://github.com/thegridelectric/gridworks-marketmaker",
    is_private=False,
    description="Runs a two-sided market associated to its GNode as part of the copper"
    "GNode sub-tree. "
    "[More on MarketMakers](https://gridworks.readthedocs.io/en/latest/market-maker.html)",
)

AtnBrickStorageHeater = GNodeStrategy(
    name=StrategyName.AtnBrickStorageHeater,
    role=GNodeRole.AtomicTNode,
    contact_email="gridworks.gridworks-consulting.com",
    repo_url="https://github.com/thegridelectric/gridworks-atn",
    is_private=False,
    description="Publicly available Dijkstra-based AtomicTNode strategy for a brick storage"
    "heater. These heaters are rooom units that store heat in a brick core, are "
    "heated with resistive elements, and typically have a fan to blow air over the"
    "brick core. They are sometimes called Electric Thermal Storage (ETS) heaters,"
    "and in the UK are often called Economy 7 heaters or Night Storage Heaters."
    "A strategy very similar to this was used by VCharge to manage an ETS fleet"
    "of several thousand heaters in Pennsylvania."
    "This strategy is meant to serve as a template for other private strategies,"
    "and also allows for an end-to-end simulation of a realistic aggregated"
    "transactive load capable of generating a highly elastic bid curve"
    "[More Info](https://gridworks-atn.readthedocs.io/en/latest/brick-storage-heater.html)",
)
