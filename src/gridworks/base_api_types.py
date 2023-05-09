""" List of all the types used"""
from typing import Dict
from typing import List
from typing import no_type_check

from gridworks.types import BaseGNodeGt_Maker
from gridworks.types import GNodeGt_Maker
from gridworks.types import GNodeInstanceGt_Maker
from gridworks.types import GwCertId_Maker
from gridworks.types import HeartbeatA_Maker
from gridworks.types import Ready_Maker
from gridworks.types import SimTimestep_Maker
from gridworks.types import SuperStarter_Maker
from gridworks.types import SupervisorContainerGt_Maker


TypeMakerByName: Dict[str, HeartbeatA_Maker] = {}


@no_type_check
def type_makers() -> List[HeartbeatA_Maker]:
    return [
        BaseGNodeGt_Maker,
        GNodeGt_Maker,
        GNodeInstanceGt_Maker,
        GwCertId_Maker,
        HeartbeatA_Maker,
        Ready_Maker,
        SimTimestep_Maker,
        SuperStarter_Maker,
        SupervisorContainerGt_Maker,
    ]


for maker in type_makers():
    TypeMakerByName[maker.type_name] = maker


def version_by_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are TypeNames, values are versions
    """

    v: Dict[str, str] = {
        "base.g.node.gt": "002",
        "g.node.gt": "002",
        "g.node.instance.gt": "000",
        "gw.cert.id": "000",
        "heartbeat.a": "100",
        "ready": "001",
        "sim.timestep": "000",
        "super.starter": "000",
        "supervisor.container.gt": "000",
    }

    return v


def status_by_versioned_type_name() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]: Keys are versioned TypeNames, values are type status
    """

    v: Dict[str, str] = {
        "base.g.node.gt.002": "Active",
        "g.node.gt.002": "Active",
        "g.node.instance.gt.000": "Active",
        "gw.cert.id.000": "Active",
        "heartbeat.a.100": "Active",
        "ready.001": "Active",
        "sim.timestep.000": "Active",
        "super.starter.000": "Active",
        "supervisor.container.gt.000": "Active",
    }

    return v
