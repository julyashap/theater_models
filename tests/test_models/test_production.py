from typing import Any

import pytest
from datetime import time

from src.models.actor import Actor
from src.models.production import Production
from src.models.type_aliases import Skills


@pytest.fixture
def production_data(actor_sample: Actor) -> dict[str, Any]:
    """"""
    return {
        "id": 1,
        "name": "Hamlet",
        "genre": "Drama",
        "roles": {"Hamlet": {"acting": 7}, "Ophelia": {"acting": 5, "singing": 3}},
        "description": "A classic Shakespeare tragedy.",
        "age_rating": 12,
        "duration": time(hour=2),
        "has_intermission": True,
        "cast": {"Hamlet": actor_sample},
    }


def test_valid_production_all_fields(production_data: dict[str, Any]) -> None:
    """"""
    production = Production(**production_data)

    assert production.id == 1
    assert production.name == "Hamlet"
    assert production.genre == "drama"
    assert "Hamlet" in production.cast
    assert production.cast["Hamlet"].name == "John"


def test_add_actor_success(production_data: dict[str, Any], actor_sample: Actor) -> None:
    """"""
    production_data["roles"] = {"Lead": {"acting": 5}, "Supporting": {"acting": 3}}
    production_data["cast"] = {}
    production = Production(**production_data)

    production.add_actor("Lead", actor_sample)
    
    assert "Lead" in production.cast
    assert production.cast["Lead"].id == actor_sample.id


def test_add_actor_unknown_role(production_data: dict[str, Any], actor_sample: Actor) -> None:
    """"""
    production = Production(**production_data)

    with pytest.raises(ValueError) as exc_info:
        production.add_actor("Villain", actor_sample)

    assert "Unknown role" in str(exc_info.value)


def test_add_actor_insufficient_skills(production_data: dict[str, Any], actor_sample: Actor) -> None:
    """"""
    production_data["roles"] = {"Lead": {"acting": 10}}
    production_data["cast"] = {}
    production = Production(**production_data)

    with pytest.raises(ValueError) as exc_info:
        production.add_actor("Lead", actor_sample)

    assert "does not fit role" in str(exc_info.value)


def test_validate_cast_missing_roles(production_data: dict[str, Any], actor_sample: Actor) -> None:
    """"""
    production = Production(**production_data)

    with pytest.raises(ValueError) as exc_info:
        production.validate_cast()

    assert "Missing actors for roles" in str(exc_info.value)


def test_format_genre_lowercase(production_data: dict[str, Any]) -> None:
    """"""
    production_data["genre"] = "TrAgEdY"
    production = Production(**production_data)

    assert production.genre == "tragedy"


def test_description_formatting(production_data: dict[str, Any]) -> None:
    """"""
    production_data["description"] = "A" * 200
    production = Production(**production_data)

    expected_desc_reduction = "AA..."
    assert expected_desc_reduction in str(production)
    assert expected_desc_reduction in repr(production)


def test_cast_auto_validation_on_post_init(actor_sample: Actor) -> None:
    """"""
    production = Production(
        name="Show",
        genre="comedy",
        roles={"Lead": {"acting": 5}},
        cast={"Lead": actor_sample},
    )

    assert "Lead" in production.cast
