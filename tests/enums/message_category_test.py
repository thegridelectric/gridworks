"""
Tests for enum message.category.000 from the GridWorks Type Registry.
"""

from gw.enums import MessageCategory


def test_message_category() -> None:
    assert set(MessageCategory.values()) == {
        "Unknown",
        "RabbitJsonDirect",
        "RabbitJsonBroadcast",
        "RabbitGwSerial",
        "MqttJsonBroadcast",
        "RestApiPost",
        "RestApiPostResponse",
        "RestApiGet",
    }

    assert MessageCategory.default() == MessageCategory.Unknown
    assert MessageCategory.enum_name() == "message.category"
    assert MessageCategory.enum_version() == "000"

    assert MessageCategory.version("Unknown") == "000"
    assert MessageCategory.version("RabbitJsonDirect") == "000"
    assert MessageCategory.version("RabbitJsonBroadcast") == "000"
    assert MessageCategory.version("RabbitGwSerial") == "000"
    assert MessageCategory.version("MqttJsonBroadcast") == "000"
    assert MessageCategory.version("RestApiPost") == "000"
    assert MessageCategory.version("RestApiPostResponse") == "000"
    assert MessageCategory.version("RestApiGet") == "000"

    for value in MessageCategory.values():
        symbol = MessageCategory.value_to_symbol(value)
        assert MessageCategory.symbol_to_value(symbol) == value
