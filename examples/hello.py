from gridworks.actor_base import ActorBase
from gridworks.enums import GNodeRole
from gridworks.enums import MessageCategory
from gridworks.gw_config import GNodeSettings
from gridworks.types import HeartbeatA_Maker


class HelloGNode(ActorBase):
    def __init__(self, settings: GNodeSettings):
        super().__init__(settings=settings)
        self.settings: GNodeSettings = settings

    def prepare_for_death(self) -> None:
        self.actor_main_stopped = True


def demo():
    settings = GNodeSettings()

    settings.g_node_alias = "d1.hello"
    settings.g_node_role_value = "GNode"

    gn = HelloGNode(settings=settings)
    gn.start()

    input(
        f"Go to http://0.0.0.0:15672/#/queues and wait for the d1.hello-Fxxxx queue to appear."
    )
    assert gn.g_node_role == GNodeRole.GNode
    hb = HeartbeatA_Maker(my_hex=0, your_last_hex="a").tuple

    print("Broadcasting a heartbeat on rabbitmq")
    gn.send_message(payload=hb, message_category=MessageCategory.RabbitJsonBroadcast)

    print("Inpsect the dummy ear queue to examine the message (click on GetMessage)")
    input("http://0.0.0.0:15672/#/queues/d1__1/dummy_ear_q")
    input(f"Hit return to tear down the GNode rabbit actor")
    gn.stop()


if __name__ == "__main__":
    demo()
