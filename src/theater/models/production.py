from datetime import time
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing_extensions import Annotated

from .actor import Actor
from .type_aliases import DisplayName, ModelID, Skills

Description = Annotated[str | None, Field(default=None, min_length=1)]


class Production(BaseModel):
    """Модель постановки."""

    id: ModelID
    name: DisplayName
    genre: Literal["drama", "comedy", "musical", "tragedy", "other"]

    roles: dict[str, Skills]

    description: Description
    age_rating: Annotated[int, Field(default=0, ge=0, le=18)]
    duration: Annotated[time, Field(default=time(hour=1))]
    has_intermission: Annotated[bool, Field(default=True)]

    cast: Annotated[dict[str, Actor], Field(default_factory=dict)]

    model_config = ConfigDict(str_strip_whitespace=True)

    def model_post_init(self, __context: Any) -> None:
        """Заполненяет поле cast с валидацией."""
        if self.cast:
            original_cast = self.cast
            self.cast = {}

            self.add_actors(original_cast)

    @field_validator("genre", mode="before")
    @classmethod
    def format_genre_lowercase(cls, v: Any) -> Any:
        """Приводит переданный жанр в строчный формат."""
        if isinstance(v, str):
            v = v.lower()
        return v

    def add_actor(self, role: str, actor: Actor) -> None:
        """Добавляет одного актера в словарь."""
        if role in self.cast:
            raise ValueError(f"Role '{role}' already assigned!")

        self._check_actor_fits_role(role, actor)
        self.cast[role] = actor

    def add_actors(self, cast: dict[str, Actor]) -> None:
        """Добавляет несколько актеров в словарь."""
        for role, actor in cast.items():
            self.add_actor(role, actor)

    def validate_cast(self) -> None:
        """Проверяет, все ли роли заполнены."""
        missing_roles = set(self.roles) - set(self.cast)

        if missing_roles:
            raise ValueError(f"Missing actors for roles: {missing_roles}!")

    def _check_actor_fits_role(self, role: str, actor: Actor) -> None:
        """Проверяет, подходит ли актер на роль."""
        if role not in self.roles:
            raise ValueError(f"Unknown role: {role}!")

        requirements = self.roles[role]

        for skill, required_level in requirements.items():
            actual_level = actor.skills.get(skill, 0)

            if actual_level < required_level:
                raise ValueError(
                    f"Actor {actor.id} does not fit role '{role}': "
                    f"{skill} {actual_level} < {required_level}"
                )

    def _format_description(self) -> str:
        """Возвращает отформатированное описание."""
        if self.description is None:
            return ""
        return (
            self.description
            if len(self.description) <= 97
            else self.description[:97] + "..."
        )

    def __str__(self) -> str:
        """Переопределяет запись поля описания в строковом представлении."""
        base = super().__str__()
        return base.replace(
            f"description={self.description!r}",
            f"description={self._format_description()!r}",
        )

    def __repr__(self) -> str:
        """Переопределяет запись поля описания в строке для разработчика."""
        base = super().__repr__()
        return base.replace(
            f"description={self.description!r}",
            f"description={self._format_description()!r}",
        )
