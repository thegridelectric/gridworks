import enum
from typing import Any
from typing import Sequence


class GwStrEnum(str, enum.Enum):
    """
    Mimics fastapi-utils use of StrEnum, which diverges from the
    python-native StrEnum for python 3.11+.  Specifically if

    class Foo(GwStrEnum):
        Bar = auto()

    then

    Foo.Bar.value is 'Bar'

    """

    @staticmethod
    def _generate_next_value_(
        name: Any, start: int, count: int, last_values: Sequence[Any]
    ) -> str:
        return str(name)
