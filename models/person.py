from typing_extensions import Annotated

from pydantic import BaseModel, ConfigDict, Field, EmailStr

from type_aliases import ModelID, DisplayName

PhoneNumber = Annotated[
    str | None, Field(default=None, pattern=r"^\+\d{1,3}\s?\d{4,14}$")
]


class Person(BaseModel):
    """Базовый класс человека."""

    id: ModelID
    name: DisplayName
    surname: DisplayName
    email_address: EmailStr

    phone_number: PhoneNumber

    model_config = ConfigDict(str_strip_whitespace=True)
