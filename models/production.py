from datetime import time
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated

from models.actor import Actor
from models.type_aliases import DisplayName, ModelID

Description = Annotated[str | None, Field(default=None, min_length=10, max_length=500)]


class Production(BaseModel):
    """Модель постановки."""

    id: ModelID
    name: DisplayName
    genre: Literal["drama", "comedy", "musical", "tragedy", "other"]

    actors: list[Actor]

    description: Description
    age_rating: Annotated[int, Field(default=0, ge=0, le=18)]
    duration: Annotated[time, Field(default=time(hour=1))]
    has_intermission: Annotated[bool, Field(default=True)]

    model_config = ConfigDict(str_strip_whitespace=True)

    @field_validator("genre", mode="before")
    @classmethod
    def format_genre_lowercase(cls, v: Any) -> Any:
        """Приводит переданный жанр в строчный формат."""
        if isinstance(v, str):
            v = v.lower()
        return v

    @field_validator("actors")
    @classmethod
    def check_unique_actors(cls, v: Any) -> Any:
        """Проверяет, есть ли в списке актеров повторения."""
        if len(v) != len({actor.id for actor in v}):
            raise ValueError("Actors must be unique!")
        return v
