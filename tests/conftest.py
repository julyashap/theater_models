import pytest

from src.models.actor import Actor
from src.models.production import Production
from src.utils.id_generator import IDGenerator


@pytest.fixture(autouse=True)
def reset_id_generator() -> None:
    """"""
    IDGenerator.instance = None
    IDGenerator.counter = 0


@pytest.fixture
def actor_sample() -> Actor:
    """"""
    return Actor(
        id=1,
        name="John",
        surname="Doe",
        email_address="john.doe@mail.com",
        phone_number="+79170000000",
        passport_number="1234567890",
        skills={"acting": 8, "singing": 5},
    )


@pytest.fixture
def production_sample(actor_sample: Actor) -> Production:
    """"""
    return Production(
        id=1,
        name="Hamlet",
        genre="drama",
        roles={"Hamlet": {"acting": 7}, "Ophelia": {"acting": 5}},
        cast={"Hamlet": actor_sample},
    )
