import copy
import time
from typing import List
from typing import Optional

import datetime
from pika.channel import Channel as PikaChannel
from pydantic import BaseModel

from gridworks.actor_base import ActorBase  # TODO: from gwatn import ActorBase
from gridworks.actor_base import RabbitRole
from gridworks.enums import GNodeRole
from gridworks.gw_config import GNodeSettings
from gridworks.types import HeartbeatA
from gridworks.types import Ready
from gridworks.types import Ready_Maker


class ExchangeBinding(BaseModel):
    From: str
    To: str
    Key: str


def load_rabbit_exchange_bindings(ch: PikaChannel) -> None:
    """
    Creation of exchanges and bindings for use in rabbit broker;
    useful if/when the definitions cannot be imported via json in ci
    - which happened for us with github actions
    :param PikaChannel ch: any open channel to the rabbit broker
    """
    if ch is None:
        raise Exception(f"Channel is None! Make sure you have started the actor")
    if not ch.is_open:
        raise Exception(
            f"Channel is not open yet! Make sure the channel is open before calling"
        )

    ch.exchange_declare(
        exchange="ear_tx",
        exchange_type="topic",
        durable=True,
        internal=True,
    )

    for role in RabbitRole.values():
        ch.exchange_declare(
            exchange=f"{role}_tx",
            exchange_type="topic",
            durable=True,
            internal=True,
        )
        ch.exchange_declare(
            exchange=f"{role}mic_tx",
            exchange_type="topic",
            durable=True,
            internal=False,
        )

    bindings: List[ExchangeBinding] = [
        ExchangeBinding(From="atomictnode", To="ear", Key="#"),
        ExchangeBinding(
            From="atomictnode",
            To="supervisor",
            Key="*.*.atomictnode.*.supervisor.*",
        ),
        ExchangeBinding(
            From="atomictnode",
            To="timecoordinator",
            Key="*.*.atomictnode.*.timecoordinator.*",
        ),
        ExchangeBinding(From="gnode", To="ear", Key="#"),
        ExchangeBinding(From="gnode", To="supervisor", Key="*.*.gnode.*.supervisor.*"),
        ExchangeBinding(
            From="gnode", To="timecoordinator", Key="*.*.gnode.*.timecoordinator.*"
        ),
        ExchangeBinding(From="marketmaker", To="ear", Key="#"),
        ExchangeBinding(
            From="marketmaker",
            To="supervisor",
            Key="*.*.marketmaker.*.supervisor.*",
        ),
        ExchangeBinding(
            From="marketmaker",
            To="timecoordinator",
            Key="*.*.marketmaker.*.timecoordinator.*",
        ),
        ExchangeBinding(From="supervisor", To="ear", Key="#"),
        ExchangeBinding(
            From="supervisor",
            To="atomictnode",
            Key="*.*.supervisor.*.atomictnode.*",
        ),
        ExchangeBinding(
            From="supervisor",
            To="marketmaker",
            Key="*.*.supervisor.*.marketmaker.*",
        ),
        ExchangeBinding(
            From="supervisor", To="supervisor", Key="*.*.supervisor*.supervisor.*"
        ),
        ExchangeBinding(
            From="supervisor",
            To="timecoordinator",
            Key="*.*.supervisor.*.timecoordinator.*",
        ),
        ExchangeBinding(From="world", To="ear", Key="#"),
        ExchangeBinding(
            From="world", To="timecoordinator", Key="*.*.world.*.timecoordinator.*"
        ),
    ]

    for binding in bindings:
        ch.exchange_bind(
            destination=f"{binding.To}_tx",
            source=f"{binding.From}mic_tx",
            routing_key=binding.Key,
        )


class GNodeStubRecorder(ActorBase):
    messages_received: int = 0
    messages_routed_internally: int = 0
    latest_from_role: Optional[str] = None
    latest_from_alias: Optional[str] = None
    latest_payload: Optional[HeartbeatA] = None
    got_heartbeat_from_super: bool = False

    def __init__(self, settings: GNodeSettings):
        super().__init__(settings=settings)
        self.settings = settings

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        self.messages_received += 1
        super().on_message(_unused_channel, basic_deliver, properties, body)

    def route_message(self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA):
        self.messages_routed_internally += 1
        self.latest_payload = payload
        if isinstance(payload, HeartbeatA):
            self.heartbeat_a_received(from_alias, from_role, payload)

    def heartbeat_a_received(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA
    ):
        if (
            from_alias == self.settings.my_super_alias
            and from_role == GNodeRole.Supervisor
        ):
            self.got_heartbeat_from_super = True

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True

    def summary_str(self):
        """Summarize results in a string"""
        return (
            f"{self.g_node_role.value} [{self.alias}] messages_received: {self.messages_received}  "
            f"latest_payload: {self.latest_payload}"
        )


class SupervisorStubRecorder(GNodeStubRecorder):
    got_heartbeat_from_sub: bool = False

    def __init__(self, settings: GNodeSettings, subordinate_alias: str):
        my_settings = copy.deepcopy(settings)
        my_settings.g_node_alias = "d1.super"
        my_settings.g_node_role_value = "Supervisor"
        super().__init__(settings=my_settings)
        self.my_single_sub = subordinate_alias

    def heartbeat_a_received(
        self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA
    ):
        """Used to test that a Supervisor gets a message from GNode"""
        if from_alias == self.my_single_sub:
            self.got_heartbeat_from_sub = True


class TimeCoordinatorStubRecorder(GNodeStubRecorder):
    """This stub timecoordinator is intended to be used"""

    def __init__(self, settings: GNodeSettings):
        self._time: int = int(datetime.datetime(
            year=2020, month=1, day=1, hour=5, tzinfo=datetime.timezone.utc
        ).timestamp())
        my_settings = copy.deepcopy(settings)
        my_settings.g_node_alias = "d1.time"
        my_settings.g_node_role_value = "TimeCoordinator"
        super().__init__(settings=my_settings)
        self.my_actors: List[str] = [GNodeSettings().g_node_alias]
        self.ready: List[str] = []

    def route_message(self, from_alias: str, from_role: GNodeRole, payload: Ready):
        if payload.TypeName == Ready_Maker.type_name:
            if from_alias in self.my_actors:
                if payload.TimeUnixS == self._time:
                    self.ready.append(from_alias)

    def is_ready(self) -> bool:
        if set(self.ready) == set(self.my_actors):
            return True
        return False

    def prepare_for_death(self):
        self.actor_main_stopped = True
