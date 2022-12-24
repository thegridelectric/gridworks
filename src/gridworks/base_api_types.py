""" List of all the types used"""
from typing import Dict
from typing import List
from typing import no_type_check

from gridworks.schemata import GNodeGt_Maker
from gridworks.schemata import GNodeInstanceGt_Maker
from gridworks.schemata import HeartbeatA_Maker
from gridworks.schemata import Ready_Maker
from gridworks.schemata import SimTimestep_Maker
from gridworks.schemata import SuperStarter_Maker
from gridworks.schemata import SupervisorContainerGt_Maker


TypeMakerByName: Dict[str, HeartbeatA_Maker] = {}


@no_type_check
def type_makers() -> List[HeartbeatA_Maker]:
    return [
        GNodeGt_Maker,
        GNodeInstanceGt_Maker,
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
        "g.node.gt": "000",
        "g.node.instance.gt": "000",
        "heartbeat.a": "001",
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
        "g.node.gt.000": "Pending",
        "g.node.instance.gt.000": "Pending",
        "heartbeat.a.001": "Pending",
        "ready.001": "Pending",
        "sim.timestep.000": "Pending",
        "super.starter.000": "Pending",
        "supervisor.container.gt.000": "Pending",
    }

    return v
