import pytest

from src.models.actor import Actor
from src.models.type_aliases import Skills
from src.services.actor import can_play_role, filter_actors_for_role


@pytest.fixture
def actor_weak() -> Actor:
    """Объект Actor с низкими навыками."""
    return Actor(
        id=2,
        name="Weak",
        surname="Actor",
        email_address="weak@mail.com",
        phone_number="+79171112233",
        passport_number="0987654321",
        skills={"acting": 3, "singing": 1},
    )


def test_can_play_role_success(actor_sample: Actor) -> None:
    """Проверяет успешный случай, когда актер подходит на роль."""
    required = {"acting": 5}

    assert can_play_role(actor_sample, required) is True


def test_can_play_role_fail(actor_sample: Actor) -> None:
    """Проверяет случай, когда актер не подходит на роль."""
    required = {"acting": 9}

    assert can_play_role(actor_sample, required) is False


def test_can_play_role_missing_skill(actor_sample: Actor) -> None:
    """Проверяет случай, когда у актера нет нужного навыка."""
    required = {"dancing": 1}

    assert can_play_role(actor_sample, required) is False


def test_filter_actors_for_role(actor_sample: Actor, actor_weak: Actor) -> None:
    """Проверяет фильтрацию актеров, подходящих на роль."""
    actors = [actor_sample, actor_weak]
    required = {"acting": 5}
    filtered = filter_actors_for_role(actors, required)
    assert filtered == [actor_sample]

    required_2 = {"acting": 2}
    filtered_2 = filter_actors_for_role(actors, required_2)
    assert {actor.id for actor in filtered_2} == {actor_sample.id, actor_weak.id}

    required_3 = {"acting": 10}
    filtered_3 = filter_actors_for_role(actors, required_3)
    assert filtered_3 == []
