from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import Annotated

from models.type_aliases import DisplayName, ModelID

PhoneNumber = Annotated[
    str | None, Field(default=None, pattern=r"^\+\d{1,3}\s?\d{4,14}$")
]


class Viewer(BaseModel):
    """Модель зрителя."""

    id: ModelID
    name: DisplayName
    surname: DisplayName
    email_address: Annotated[str, Field(pattern=r"[^@]+@[^@]+\.[^@]+")]

    ticket_number: Annotated[str, Field(min_length=8, max_length=8, pattern=r"^\d+$")]

    phone_number: PhoneNumber

    model_config = ConfigDict(str_strip_whitespace=True)
