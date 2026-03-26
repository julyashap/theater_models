from src.theater.models.actor import Actor
from src.theater.models.production import Production
from src.theater.services.production import get_actor_by_role, get_cast_list, get_missing_roles


def test_get_missing_roles(production_sample: Production) -> None:
    """Проверяет возврат незаполненных ролей."""
    missing = get_missing_roles(production_sample)

    assert missing == {"Ophelia"}


def test_get_cast_list(production_sample: Production, actor_sample: Actor) -> None:
    """Проверяет возврат списка актеров постановки."""
    cast_list = get_cast_list(production_sample)

    assert cast_list == [actor_sample]


def test_get_actor_by_role(production_sample: Production, actor_sample: Actor) -> None:
    """Проверяет возврат актера по указанной роли."""
    actor = get_actor_by_role(production_sample, "Hamlet")
    assert actor == actor_sample

    actor_none = get_actor_by_role(production_sample, "Ophelia")
    assert actor_none is None
