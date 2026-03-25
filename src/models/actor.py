from typing import Any

from pydantic import Field, field_validator
from typing_extensions import Annotated

from models.person import Person
from models.type_aliases import Skills


class Actor(Person):
    """Модель актера."""

    passport_number: Annotated[str, Field(pattern=r"^\d{10}$")]

    skills: Skills

    @field_validator("passport_number", mode="before")
    @classmethod
    def format_passport_number(cls, v: Any) -> Any:
        """Убирает пробел в номере паспорта."""
        if isinstance(v, str):
            v = v.replace(" ", "")
        return v
