import json
from typing import Any, Dict, Literal, Type, TypeVar

from gw.errors import GwTypeError
from gw.utils import recursively_pascal, snake_to_pascal
from pydantic import BaseModel, ConfigDict, ValidationError

T = TypeVar("T", bound="GwBase")


class GwBase(BaseModel):
    type_name: Literal["gw.base"] = "gw.base"
    version: Literal["000"] = "000"

    model_config = ConfigDict(
        alias_generator=snake_to_pascal,
        frozen=True,
        populate_by_name=True,
    )

    def to_type(self) -> bytes:
        return self.model_dump_json(exclude_none=True, by_alias=True)

    def to_dict(self) -> Dict[str, Any]:
        bytes = self.model_dump_json(exclude_none=True, by_alias=True)
        return json.loads(bytes)

    @classmethod
    def from_type(cls, bytes) -> T:
        try:
            d = json.loads(bytes)
        except TypeError as e:
            raise GwTypeError("Type must be string or bytes!") from e
        return cls.from_dict(d)

    @classmethod
    def from_dict(cls: Type[T], d: dict) -> T:
        if not recursively_pascal(d):
            GwTypeError(
                f"Dictionary keys must be recursively PascalCase. "
                f"Found: {d}. Consider checking nested structures."
            )
        try:
            t = cls.model_validate(d)
        except ValidationError as e:
            raise GwTypeError(f"Validation failed for {cls.__name__}: {e}") from e
        return t

    @classmethod
    def get_schema_info(cls) -> Dict[str, Any]:
        """Return schema information for this type."""
        return {
            "type_name": cls.type_name_value(),
            "version": cls.version_value(),
            "fields": list(cls.model_fields.keys()),
        }

    def __repr__(self) -> str:
        """Provide clear representation for debugging and logging."""
        return f"{self.__class__.__name__}(type_name='{self.type_name}', version='{self.version}')"

    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"{self.type_name_value()}.{self.version_value()}"

    @classmethod
    def type_name_value(cls) -> str:
        # Automatically return the type_name defined in the subclass
        return cls.model_fields["type_name"].default

    @classmethod
    def version_value(cls) -> str:
        # return the Version defined in the subclass
        return cls.model_fields["version"].default
