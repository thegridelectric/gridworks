import time
from typing import List
from typing import Optional

import pendulum
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
    def __init__(self, settings: GNodeSettings):
        super().__init__(settings=settings)
        self.settings: GNodeSettings = settings
        self.payloads = []

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True


class SupervisorStubRecorder(GNodeStubRecorder):
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
        settings.g_node_alias = "d1.super"
        settings.g_node_role_value = "Supervisor"
        super().__init__(settings=settings)

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        self.messages_received += 1
        super().on_message(_unused_channel, basic_deliver, properties, body)

    def route_message(self, from_alias: str, from_role: GNodeRole, payload: HeartbeatA):
        self.messages_routed_internally += 1
        self.latest_payload = payload
        if isinstance(payload, HeartbeatA):
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


class TimeCoordinatorStubRecorder(GNodeStubRecorder):
    """This stub timecoordinator is intended to be used"""

    def __init__(self, settings: GNodeSettings):
        self._time: int = pendulum.datetime(
            year=2020, month=1, day=1, hour=5
        ).int_timestamp
        settings.g_node_alias = "d1.time"
        settings.g_node_role_value = "TimeCoordinator"
        super().__init__(settings=settings)
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
