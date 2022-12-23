import time
import uuid
from typing import Callable
from typing import List
from typing import Optional

import pendulum
import pika
from pydantic import BaseModel

from gridworks.actor_base import ActorBase
from gridworks.actor_base import OnSendMessageDiagnostic
from gridworks.actor_base import RabbitRole
from gridworks.enums import GNodeRole
from gridworks.enums import MessageCategory
from gridworks.gw_config import GNodeSettings
from gridworks.schemata import HeartbeatA
from gridworks.schemata import HeartbeatA_Maker
from gridworks.schemata import Ready
from gridworks.schemata import Ready_Maker
from gridworks.schemata import SimTimestep
from gridworks.schemata import SimTimestep_Maker


class ExchangeBinding(BaseModel):
    From: str
    To: str
    Key: str


class GNodeStubRecorder(ActorBase):
    def __init__(self, settings: GNodeSettings):
        super().__init__(settings=settings)
        self.settings: GNodeSettings = settings
        self.payloads = []

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True

    def load_rabbit_exchange_bindings(self):
        ch = self._consume_channel

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
        time.sleep(1)
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
            ExchangeBinding(
                From="gnode", To="supervisor", Key="*.*.gnode.*.supervisor.*"
            ),
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

    ########################
    ## Receives
    ########################


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


class TimeCoordinatorStubRecorder(ActorBase):
    def __init__(self, settings: GNodeSettings):
        self._time: int = pendulum.datetime(
            year=2020, month=1, day=1, hour=5
        ).int_timestamp
        settings.g_node_alias = "d1.time"
        settings.g_node_role_value = "TimeCoordinator"
        super().__init__(settings=settings)
        self.gnode_ready: bool = False

    def route_message(self, from_alias: str, from_role: GNodeRole, payload: Ready):
        if payload.TypeName == Ready_Maker.type_name:
            if from_alias == GNodeSettings().g_node_alias:
                self.gnode_ready = True

    def prepare_for_death(self):
        self.actor_main_stopped = True


def wait_for(
    f: Callable[[], bool],
    timeout: float,
    tag: str = "",
    raise_timeout: bool = True,
    retry_duration: float = 0.1,
) -> bool:
    """Call function f() until it returns True or a timeout is reached. retry_duration specified the sleep time between
    calls. If the timeout is reached before f return True, the function will either raise a ValueError (the default),
    or, if raise_timeout==False, it will return False. Function f is guaranteed to be called at least once. If an
    exception is raised the tag string will be attached to its message.
    """
    now = time.time()
    until = now + timeout
    if now >= until:
        if f():
            return True
    while now < until:
        if f():
            return True
        now = time.time()
        if now < until:
            time.sleep(min(retry_duration, until - now))
            now = time.time()
    if raise_timeout:
        raise ValueError(
            f"ERROR. Function {f} timed out after {timeout} seconds. {tag}"
        )
    else:
        return False
