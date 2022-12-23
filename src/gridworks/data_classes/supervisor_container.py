""" SupervisorContainer  Definition """
import logging
from typing import Dict

from gridworks.enums import SupervisorContainerStatus


LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)

LOGGER.setLevel(logging.INFO)


class SupervisorContainer:
    by_id: Dict[str, "SupervisorContainer"] = {}

    def __new__(cls, supervisor_container_id: str, *args, **kwargs) -> "SupervisorContainer":  # type: ignore
        try:
            return cls.by_id[supervisor_container_id]
        except KeyError:
            instance = super().__new__(cls)
            cls.by_id[supervisor_container_id] = instance
            return instance

    def __init__(
        self,
        supervisor_container_id: str,
        status: SupervisorContainerStatus,
        world_instance_alias: str,
        supervisor_g_node_instance_id: str,
        supervisor_g_node_alias: str,
    ):
        self.supervisor_container_id = supervisor_container_id
        self.status = status
        self.world_instance_alias = world_instance_alias
        self.supervisor_g_node_instance_id = supervisor_g_node_instance_id
        self.supervisor_g_node_alias = supervisor_g_node_alias
