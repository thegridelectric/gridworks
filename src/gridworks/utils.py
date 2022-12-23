import logging
import re
import time
from typing import Any
from typing import Optional
from typing import no_type_check

import pendulum
from pydantic import BaseModel

import gridworks.property_format as property_format
from gridworks.enums import MessageCategory
from gridworks.enums import MessageCategorySymbol
from gridworks.errors import SchemaError


DEFAULT_STEP_DURATION = 0.1

LOG_FORMAT = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)
LOGGER = logging.getLogger(__name__)


class RestfulResponse(BaseModel):
    Note: str
    HttpStatusCode: int = 200
    PayloadTypeName: Optional[str] = None
    PayloadAsDict: Optional[Any] = None


snake_add_underscore_to_camel_pattern = re.compile(r"(?<!^)(?=[A-Z])")


def camel_to_snake(name: str) -> str:
    return snake_add_underscore_to_camel_pattern.sub("_", name).lower()


def snake_to_camel(word: str) -> str:
    return "".join(x.capitalize() or "_" for x in word.split("_"))


def dot_to_underscore(candidate: str) -> str:
    """Translation between two different formats for a list of alphanumeric
    words (where the most significant word does not start with a number).

    Args:
        candidate (str): left-right-dot format. Most significant word on the
        left, word seperators are periods.

    Raises:
        SchemaError: if input is not left-right-dot format

    Returns:
        str:  Same string in LRU format. Seperator is now underscore, most
        significant word still on the left.
    """
    try:
        property_format.check_is_lrd_alias_format(candidate)
    except SchemaError as e:
        raise SchemaError(f"{candidate} not LrdAliasFormat: {e}!")

    return candidate.replace(".", "_")


def underscore_to_dot(candidate: str) -> str:
    """Replaces underscores to dots in a string, checking that all words between
    seperators are alphanumeric.
    """
    if property_format.is_lru_alias_format(candidate):
        return candidate.replace("_", ".")
    else:
        raise SchemaError(
            f"{candidate} words with underscore as separator are not alphanumeric!"
        )


def message_category_from_symbol(symbol: MessageCategorySymbol) -> MessageCategory:
    category = MessageCategory.Unknown
    if symbol == MessageCategorySymbol.rj:
        category = MessageCategory.RabbitJsonDirect
    elif symbol == MessageCategorySymbol.rjb:
        category = MessageCategory.RabbitJsonBroadcast
    elif symbol == MessageCategorySymbol.s:
        category = MessageCategory.RabbitGwSerial
    elif symbol == MessageCategorySymbol.gw:
        category = MessageCategory.MqttJsonBroadcast
    elif symbol == MessageCategorySymbol.post:
        category = MessageCategory.RestApiPost
    elif symbol == MessageCategorySymbol.postack:
        category = MessageCategory.RestApiPostResponse
    elif symbol == MessageCategorySymbol.get:
        category = MessageCategory.RestApiGet
    return category


def responsive_sleep(
    obj: Any,
    seconds: float,
    step_duration: float = DEFAULT_STEP_DURATION,
    running_field_name: str = "_main_loop_running",
) -> bool:
    """Sleep in way that is more responsive to thread termination: sleep in step_duration increments up to
    specificed seconds, at after each step checking self._main_loop_running"""
    sleeps = int(seconds / step_duration)
    if sleeps * step_duration != seconds:
        last_sleep = seconds - (sleeps * step_duration)
    else:
        last_sleep = 0
    for _ in range(sleeps):
        if getattr(obj, running_field_name):
            time.sleep(step_duration)
    if getattr(obj, running_field_name) and last_sleep > 0:
        time.sleep(last_sleep)
    return getattr(obj, running_field_name)  # type: ignore[no-any-return]


class MessageSummary:
    """Helper class for formating message summaries message receipt/publication single line summaries."""

    DEFAULT_FORMAT = (
        "{timestamp}  {direction:4s}  {actor_alias:33s}  {broker_flag}  {arrow:2s}  {topic:80s}"
        "  {payload_type}"
    )

    @no_type_check
    @classmethod
    def format(
        cls,
        direction: str,
        actor_alias: str,
        topic: str,
        payload_object: Any = None,
        broker_flag=" ",
        timestamp: Optional[pendulum.datetime] = None,
    ) -> str:
        """
        Formats a single line summary of message receipt/publication.

        Args:
            direction: "IN" or "OUT"
            actor_alias: The node alias of the sending or receiving actor.
            topic: The destination or source topic.
            payload_object: The payload of the message.
            broker_flag: "*" for the "gw" broker.
            timestamp: "pendulum.now("UTC") by default.

        Returns:
            Formatted string.
        """
        try:
            if timestamp is None:
                timestamp = pendulum.now("UTC")
            direction = direction[:3].strip().upper()
            if direction in ["OUT", "SND"]:
                arrow = "->"
            elif direction.startswith("IN") or direction.startswith("RCV"):
                arrow = "<-"
            else:
                arrow = "? "
            if hasattr(payload_object, "__class__"):
                payload_str = payload_object.__class__.__name__
            else:
                payload_str = type(payload_object)
            return cls.DEFAULT_FORMAT.format(
                timestamp=timestamp.isoformat(),
                direction=direction,
                actor_alias=actor_alias,
                broker_flag=broker_flag,
                arrow=arrow,
                topic=f"[{topic}]",
                payload_type=payload_str,
            )
        except Exception as e:
            print(f"ouch got {e}")
            return ""
