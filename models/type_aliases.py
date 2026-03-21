from uuid import uuid4

from pydantic import Field
from typing_extensions import Annotated

ModelID = Annotated[
    str, Field(min_length=4, max_length=4, default_factory=lambda: uuid4().hex[:4])
]

DisplayName = Annotated[str, Field(min_length=2, max_length=100)]
