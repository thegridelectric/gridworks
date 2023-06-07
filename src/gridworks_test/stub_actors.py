from typing import Optional

import pendulum

from gridworks.actor_base import ActorBase  # TODO: from gwatn import ActorBase
from gridworks.enums import GNodeRole
from gridworks.gw_config import GNodeSettings
from gridworks.types import HeartbeatA
from gridworks.types import Ready
from gridworks.types import Ready_Maker


class SupervisorStubRecorder(ActorBase):
    messages_received: int
    messages_routed_internally: int
    latest_from_role: Optional[str]
    latest_from_alias: Optional[str]
    latest_payload: Optional[HeartbeatA]
    routing_to_super__heartbeat_a__worked: bool = False

    def __init__(self, settings: GNodeSettings):
        self.messages_received = 0
        self.messages_routed_internally = 0
        self.latest_from_role: Optional[str] = None
        self.latest_from_alias: Optional[str] = None
        self.latest_payload: Optional[HeartbeatA] = None

        super().__init__(settings=settings)

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        self.messages_received += 1
        super().on_message(_unused_channel, basic_deliver, properties, body)

    def route_message(self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA):
        self.messages_routed_internally += 1
        self.latest_payload = payload
        self.latest_from_role = from_role
        self.latest_from_alias = from_alias

        self.heartbeat_a_received(from_alias, from_role, payload)

    def prepare_for_death(self):
        self.actor_main_stopped = True

    def heartbeat_a_received(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA
    ):
        self.routing_to_super__heartbeat_a__worked = True

    def summary_str(self):
        """Summarize results in a string"""
        return (
            f"AbstractActor [{self.alias}] messages_received: {self.messages_received}  "
            f"latest_payload: {self.latest_payload}"
        )


class TimeCoordinatorStubRecorder(ActorBase):
    def __init__(self, settings: GNodeSettings):
        self._time: int = pendulum.datetime(
            year=2020, month=1, day=1, hour=5
        ).int_timestamp
        settings.g_node_alias = "d1.time"
        settings.g_node_role_value = "TimeCoordinator"
        super().__init__(settings=settings)
        self.atn_ready: bool = False

    def route_message(self, from_alias: str, from_role: GNodeRole, payload: Ready):
        if payload.TypeName == Ready_Maker.type_name:
            if from_alias == GNodeSettings().g_node_alias:
                self.atn_ready = True

    def prepare_for_death(self):
        self.actor_main_stopped = True
