from uuid import uuid4

from pydantic import Field
from typing_extensions import Annotated

from utils.id_generator import IDGenerator

ModelID = Annotated[
    int, Field(default_factory=lambda: IDGenerator().get_id())
]

DisplayName = Annotated[str, Field(min_length=1)]
