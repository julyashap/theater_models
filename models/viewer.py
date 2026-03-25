from pydantic import Field
from typing_extensions import Annotated

from models.person import Person


class Viewer(Person):
    """Модель зрителя."""

    ticket_number: Annotated[str, Field(pattern=r"^\d{8}$")]
