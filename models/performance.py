from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, computed_field, field_validator
from typing_extensions import Annotated

from models.production import Production
from models.type_aliases import DisplayName, ModelID
from models.viewer import Viewer


class Performance(BaseModel):
    """Модель представления."""

    id: ModelID
    start_datetime: datetime
    theater_name: DisplayName
    count_tickets: Annotated[int, Field(gt=0)]

    production: Production

    is_premiere: Annotated[bool, Field(default=False)]

    viewers: Annotated[list[Viewer], Field(default_factory=list)]

    model_config = ConfigDict(str_strip_whitespace=True)

    @field_validator("viewers")
    @classmethod
    def check_unique_viewers(cls, v: Any) -> Any:
        """Проверяет, есть ли в списке зрителей повторения."""
        if v and len(v) != len({viewer.id for viewer in v}):
            raise ValueError("Viewers must be unique!")
        return v

    @computed_field
    def available_tickets(self) -> int:
        """Вычисляет количество оставшихся билетов."""
        return self.count_tickets - len(self.viewers)

    def add_viewer(self, viewer: Viewer) -> None:
        """Добавляет одного зрителя в список."""
        self._check_unique_viewer(viewer)
        self.viewers.append(viewer)

    def add_viewers(self, viewers: list[Viewer]) -> None:
        """Добавляет несколько зрителей в список."""
        for viewer in viewers:
            self._check_unique_viewer(viewer)
        self.viewers.extend(viewers)

    def _check_unique_viewer(self, viewer: Viewer) -> None:
        """Проверяет, есть ли уже зритель в списке."""
        if viewer in self.viewers:
            raise ValueError("Viewer {viewer.id} already exists in Performance {self.id}}!")
