from typing import Any, ClassVar
from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, field_validator
from models.type_aliases import ModelID, NameSurname

PassportNumber = Annotated[
    str,
    Field(
        min_length=10, 
        max_length=10, 
        pattern=r"^\d+$", 
        exclude=True
    )
]


class Actor(BaseModel):
    """Модель актера."""

    REQUIRED_SKILLS: ClassVar[set[str]] = {"diction", "vocals", "plasticity"}

    id: ModelID
    name: NameSurname
    surname: NameSurname
    passport_number: PassportNumber

    skills: dict[str, Annotated[int, Field(ge=0, le=10)]]

    model_config = ConfigDict(str_strip_whitespace=True)

    @field_validator("passport_number", mode="before")
    @classmethod
    def format_passport_number(cls, v: Any) -> Any:
        """Убирает пробел в номере паспорта."""
        if isinstance(v, str):
            v = v.replace(" ", "")
        return v

    @field_validator("skills")
    @classmethod
    def check_required_skills(cls, v: Any) -> Any:
        """Проверяет наличие обязательных навыков."""
        missing = cls.REQUIRED_SKILLS - set(v.keys())
        if missing:
            raise ValueError(
                f"Keys {missing} are required!"
            )
        return v
