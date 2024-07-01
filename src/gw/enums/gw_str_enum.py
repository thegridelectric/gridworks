import enum


class GwStrEnum(str, enum.Enum):
    """
    Mimics fastapi-utils use of StrEnum, which diverges from the
    python-native StrEnum for python 3.11+.  Specifically if

    class Foo(GwStrEnum):
        Bar = auto()

    then

    Foo.Bar.value is 'Bar'

    """

    def _generate_next_value_(name, start, count, last_values):
        return name
