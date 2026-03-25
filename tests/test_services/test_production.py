import pytest
from src.models.production import Production
from src.models.actor import Actor
from src.services.production import get_missing_roles, get_cast_list, get_actor_by_role


def test_get_missing_roles(production_sample: Production) -> None:
    """"""
    missing = get_missing_roles(production_sample)

    assert missing == {"Ophelia"}


def test_get_cast_list(production_sample: Production, actor_sample: Actor) -> None:
    """"""
    cast_list = get_cast_list(production_sample)
    
    assert cast_list == [actor_sample]


def test_get_actor_by_role(production_sample: Production, actor_sample: Actor) -> None:
    """"""
    actor = get_actor_by_role(production_sample, "Hamlet")
    assert actor == actor_sample

    actor_none = get_actor_by_role(production_sample, "Ophelia")
    assert actor_none is None
