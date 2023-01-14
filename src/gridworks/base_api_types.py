""" List of all the types used"""
from typing import Dict
from typing import List
from typing import no_type_check

from gridworks.types import GNodeGt_Maker
from gridworks.types import GNodeInstanceGt_Maker
from gridworks.types import GwCertId_Maker
from gridworks.types import HeartbeatA_Maker
from gridworks.types import InitialTadeedAlgoCreate_Maker
from gridworks.types import InitialTadeedAlgoOptin_Maker
from gridworks.types import InitialTadeedAlgoTransfer_Maker
from gridworks.types import Ready_Maker
from gridworks.types import SimTimestep_Maker
from gridworks.types import SuperStarter_Maker
from gridworks.types import SupervisorContainerGt_Maker
from gridworks.types import TavalidatorcertAlgoCreate_Maker
from gridworks.types import TavalidatorcertAlgoTransfer_Maker


TypeMakerByName: Dict[str, HeartbeatA_Maker] = {}


@no_type_check
def type_makers() -> List[HeartbeatA_Maker]:
    return [
        GNodeGt_Maker,
        GNodeInstanceGt_Maker,
        GwCertId_Maker,
        HeartbeatA_Maker,
        InitialTadeedAlgoCreate_Maker,
        InitialTadeedAlgoOptin_Maker,
        InitialTadeedAlgoTransfer_Maker,
        Ready_Maker,
        SimTimestep_Maker,
        SuperStarter_Maker,
        SupervisorContainerGt_Maker,
        TavalidatorcertAlgoCreate_Maker,
        TavalidatorcertAlgoTransfer_Maker,
    ]


for maker in type_makers():
    TypeMakerByName[maker.type_name] = maker


def version_by_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are TypeNames, values are versions
    """

    v: Dict[str, str] = {
        "g.node.gt": "001",
        "g.node.instance.gt": "000",
        "gw.cert.id": "000",
        "heartbeat.a": "100",
        "initial.tadeed.algo.create": "000",
        "initial.tadeed.algo.optin": "002",
        "initial.tadeed.algo.transfer": "000",
        "ready": "001",
        "sim.timestep": "000",
        "super.starter": "000",
        "supervisor.container.gt": "000",
        "tavalidatorcert.algo.create": "000",
        "tavalidatorcert.algo.transfer": "000",
    }

    return v


def status_by_versioned_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are versioned TypeNames, values are type status
    """

    v: Dict[str, str] = {
        "g.node.gt.001": "Pending",
        "g.node.instance.gt.000": "Pending",
        "gw.cert.id.000": "Pending",
        "heartbeat.a.100": "Pending",
        "initial.tadeed.algo.create.000": "Pending",
        "initial.tadeed.algo.optin.002": "Pending",
        "initial.tadeed.algo.transfer.000": "Pending",
        "ready.001": "Pending",
        "sim.timestep.000": "Pending",
        "super.starter.000": "Pending",
        "supervisor.container.gt.000": "Pending",
        "tavalidatorcert.algo.create.000": "Pending",
        "tavalidatorcert.algo.transfer.000": "Pending",
    }

    return v
