import time
import uuid

import datetime

from gridworks.enums import GNodeRole
from gridworks.enums import MessageCategory
from gridworks.gw_config import GNodeSettings
from gridworks.types import HeartbeatA_Maker
from gridworks.types import SimTimestep_Maker
from gridworks_test import GNodeStubRecorder
from gridworks_test import SupervisorStubRecorder
from gridworks_test import TimeCoordinatorStubRecorder
from gridworks_test import load_rabbit_exchange_bindings
from gridworks_test import wait_for


def test_actor_base():
    settings = GNodeSettings()

    gn = GNodeStubRecorder(settings)
    gn.start()
    su = SupervisorStubRecorder(settings, subordinate_alias=settings.g_node_alias)
    su.start()
    tc = TimeCoordinatorStubRecorder(settings)
    tc.start()
    wait_for(lambda: su._consuming, 4, "supervisor is consuming")
    wait_for(lambda: gn._consuming, 4, "gnode is consuming")
    wait_for(lambda: tc._consuming, 4, "timecoordinator is consuming")

    # This is required for tests to pass in CI, as we haven't figured
    # out how to pre-load the bindings and exchanges in github actions
    load_rabbit_exchange_bindings(gn._consume_channel)

    payload = HeartbeatA_Maker(my_hex="0", your_last_hex="0").tuple
    gn.send_message(
        payload=payload, to_role=GNodeRole.Supervisor, to_g_node_alias=su.alias
    )

    wait_for(lambda: su.messages_received > 0, 2, "supervisor received message")

    assert su.messages_received == 1
    assert su.messages_routed_internally == 1
    assert su.got_heartbeat_from_sub

    d = datetime.datetime(year=2020, month=1, day=1, hour=5)
    t = int(d.timestamp())
    payload = SimTimestep_Maker(
        from_g_node_alias="d1.time",
        from_g_node_instance_id=str(uuid.uuid4()),
        time_unix_s=t,
        timestep_created_ms=1000 * int(time.time()),
        message_id=str(uuid.uuid4()),
    ).tuple

    gn.stop()
    su.stop()
    tc.stop()


#     gnf = GNodeFactoryRabbitStubRecorder(settings=GnfSettings())
#     gnr = GNodeRegistryStubRecorder(settings=DevGNodeRegistrySettings())
#     payload = HeartbeatA_Maker().tuple
#     result = gnf.send_direct_message(
#         payload=payload, to_g_node_type_short_alias="gnr", to_g_node_alias="dwgps.gnr"
#     )
#     assert result == OnSendMessageDiagnostic.STOPPED_SO_NOT_SENDING

#     gnf.start()
#     gnr.start()

#     wait_for(lambda: gnf._consume_connection, 2, "actor._consume_connection exists")
#     wait_for(lambda: gnf._consuming, 2, "actor is consuming")
#     wait_for(lambda: gnf._publish_connection.is_open, 2, "actor publish connection is open")

#     assert gnf.messages_received == 0
#     assert gnf.messages_routed_internally == 0

#     ####################################
#     # Testing actor_base.on_message
#     ###################################
#     gnf._consume_channel.queue_bind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="garbage.#",
#     )
#     gnf._consume_channel.queue_bind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="pubsub.#",
#     )
#     gnf._consume_channel.queue_bind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="json",
#     )
#     gnf._consume_channel.queue_bind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="json.*.crap.*.*",
#     )
#     time.sleep(0.5)

#     payload = HeartbeatA_Maker().tuple

#     properties = pika.BasicProperties(
#         reply_to=gnr.queue_name,
#         app_id=gnr.alias,
#         correlation_id=str(uuid.uuid4()),
#     )
#     gnr._publish_channel.basic_publish(
#         exchange=gnr._publish_exchange,
#         routing_key="garbage.first_word_does_not_encode_recognized_routing_key_type",
#         body=payload.as_type(),
#         properties=properties,
#     )

#     wait_for(
#         lambda: gnf.messages_received == 1, 2, f"gnf.messages_received is {gnf.messages_received}"
#     )
#     assert gnf.messages_received == 1
#     assert gnf.messages_routed_internally == 0
#     assert (
#         gnf._latest_on_message_diagnostic == OnReceiveMessageDiagnostic.TYPE_NAME_DECODING_PROBLEM
#     )

#     properties = pika.BasicProperties(
#         reply_to=gnr.queue_name,
#         app_id=gnr.alias,
#         type=RoutingKeyType.GW_PUBSUB.value,
#         correlation_id=str(uuid.uuid4()),
#     )

#     gnr._publish_channel.basic_publish(
#         exchange=gnr._publish_exchange,
#         routing_key="pubsub.dwgps_gnr.the_latest_scoop_everybody_wants",
#         body=payload.as_type(),
#         properties=properties,
#     )
#     wait_for(
#         lambda: gnf.messages_received == 2, 2, f"gnf.messages_received is {gnf.messages_received}"
#     )
#     assert gnf.messages_received == 2
#     assert gnf.messages_routed_internally == 0
#     assert (
#         gnf._latest_on_message_diagnostic == OnReceiveMessageDiagnostic.UNHANDLED_ROUTING_KEY_TYPE
#     )

#     properties = pika.BasicProperties(
#         reply_to=gnr.queue_name,
#         app_id=gnr.alias,
#         type=RoutingKeyType.JSON_DIRECT_MESSAGE.value,
#         correlation_id=str(uuid.uuid4()),
#     )
#     gnr._publish_channel.basic_publish(
#         exchange=gnr._publish_exchange,
#         routing_key="json.dwgps_gnr.gnr.gnf.dwgps_gnf",
#         body=json.dumps({"TypeName": "not.lrd.format_bro"}),
#         properties=properties,
#     )
#     wait_for(
#         lambda: gnf.messages_received == 3, 2, f"gnf.messages_received is {gnf.messages_received}"
#     )
#     assert gnf.messages_received == 3
#     assert gnf.messages_routed_internally == 0
#     assert (
#         gnf._latest_on_message_diagnostic == OnReceiveMessageDiagnostic.TYPE_NAME_DECODING_PROBLEM
#     )

#     properties = pika.BasicProperties(
#         reply_to=gnr.queue_name,
#         app_id=gnr.alias,
#         type=RoutingKeyType.JSON_DIRECT_MESSAGE.value,
#         correlation_id=str(uuid.uuid4()),
#     )
#     gnr._publish_channel.basic_publish(
#         exchange=gnr._publish_exchange,
#         routing_key="json.dwgps_gnr.gnr.gnf.dwgps_gnf",
#         body=json.dumps({"TypeName": "esoteric.type.alias.100"}),
#         properties=properties,
#     )
#     wait_for(
#         lambda: gnf.messages_received == 4, 2, f"gnf.messages_received is {gnf.messages_received}"
#     )
#     assert gnf.messages_received == 4
#     assert gnf.messages_routed_internally == 0
#     assert gnf._latest_on_message_diagnostic == OnReceiveMessageDiagnostic.UNKNOWN_type_name

#     gnr._publish_channel.basic_publish(
#         exchange=gnr._publish_exchange,
#         routing_key="json",
#         body=payload.as_type(),
#         properties=properties,
#     )
#     wait_for(
#         lambda: gnf.messages_received == 5, 2, f"gnf.messages_received is {gnf.messages_received}"
#     )
#     assert gnf.messages_received == 5
#     assert gnf.messages_routed_internally == 0
#     assert (
#         gnf._latest_on_message_diagnostic == OnReceiveMessageDiagnostic.FROM_GNODE_DECODING_PROBLEM
#     )

#     gnr._publish_channel.basic_publish(
#         exchange=gnr._publish_exchange,
#         routing_key="json.bad-from_g_node_alias.gnr.gnf.dwgps_gnf",
#         body=payload.as_type(),
#         properties=properties,
#     )
#     wait_for(
#         lambda: gnf.messages_received == 6, 2, f"gnf.messages_received is {gnf.messages_received}"
#     )
#     assert gnf.messages_received == 6
#     assert gnf.messages_routed_internally == 0
#     assert (
#         gnf._latest_on_message_diagnostic == OnReceiveMessageDiagnostic.FROM_GNODE_DECODING_PROBLEM
#     )

#     gnr._publish_channel.basic_publish(
#         exchange=gnr._publish_exchange,
#         routing_key="json.dwgps_gnr.crap.gnf.dwgps_gnf",
#         body=payload.as_type(),
#         properties=properties,
#     )
#     wait_for(
#         lambda: gnf.messages_received == 6, 2, f"gnf.messages_received is {gnf.messages_received}"
#     )
#     assert gnf.messages_received == 6
#     assert gnf.messages_routed_internally == 0
#     assert (
#         gnf._latest_on_message_diagnostic == OnReceiveMessageDiagnostic.FROM_GNODE_DECODING_PROBLEM
#     )

#     gnf._consume_channel.queue_unbind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="garbage.#",
#     )
#     gnf._consume_channel.queue_unbind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="pubsub.#",
#     )
#     gnf._consume_channel.queue_unbind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="json",
#     )
#     gnf._consume_channel.queue_unbind(
#         gnf.queue_name,
#         "gnrmic_tx",
#         routing_key="json.*.crap.*.*",
#     )

#     ####################################
#     # Testing actor_base.send_direct_message
#     ###################################

#     gnf._stopping = True
#     result = gnf.send_direct_message(
#         payload=payload, to_g_node_type_short_alias="gnr", to_g_node_alias="dwgps.gnr"
#     )
#     assert result == OnSendMessageDiagnostic.STOPPING_SO_NOT_SENDING
#     gnf._stopping = False

#     gnf._publish_channel.close()

#     gnf._publish_channel = None
#     result = gnf.send_direct_message(
#         payload=payload,
#         to_g_node_type_short_alias="gnr",
#         to_g_node_alias="dwgps.gnr",
#     )
#     assert result == OnSendMessageDiagnostic.CHANNEL_NOT_OPEN

#     gnf._publish_channel = None
#     result = gnf.send_direct_message(
#         payload=payload,
#         to_g_node_type_short_alias="gnr",
#         to_g_node_alias="dwgps.gnr",
#     )
#     assert result == OnSendMessageDiagnostic.CHANNEL_NOT_OPEN

#     gnr.stop()
#     gnf.stop()
