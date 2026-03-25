from typing import Any

import pytest

from src.models.actor import Actor


@pytest.fixture
def actor_data() -> dict[str, Any]:
    """"""
    return {
        "id": 1,
        "name": "Name",
        "surname": "Surname",
        "email_address": "example@mail.com",
        "phone_number": "+79171985623",
        "passport_number": "1234567890",
        "skills": {"acting": 8, "singing": 5},
    }


def test_valid_actor_all_fields(actor_data: dict[str, Any]) -> None:
    """"""
    actor = Actor(**actor_data)

    assert actor.id == 1
    assert actor.name == "Name"
    assert actor.surname == "Surname"
    assert actor.passport_number == "1234567890"
    assert actor.skills == {"acting": 8, "singing": 5}


def test_invalid_actor_passport_number(actor_data: dict[str, Any]) -> None:
    """"""
    actor_data["passport_number"] = "1234 ABCD"

    with pytest.raises(ValueError) as exc_info:
        Actor(**actor_data)

    str_exc_value = str(exc_info.value)
    assert "passport_number" in str_exc_value
    assert "String should match pattern" in str_exc_value


def test_actor_passport_number_autoformat(actor_data: dict[str, Any]) -> None:
    """"""
    actor_data["passport_number"] = "12 34 56 78 90"
    
    actor = Actor(**actor_data)
    
    assert actor.passport_number == "1234567890"


def test_invalid_actor_skills_range(actor_data: dict[str, Any]) -> None:
    """"""
    actor_data["skills"]["acting"] = 15

    with pytest.raises(ValueError) as exc_info:
        Actor(**actor_data)

    str_exc_value = str(exc_info.value)
    assert "skills" in str_exc_value
    assert "Input should be less than or equal to 10" in str_exc_value


def test_invalid_actor_skills_type(actor_data: dict[str, Any]) -> None:
    """"""
    actor_data["skills"]["acting"] = "high"

    with pytest.raises(ValueError) as exc_info:
        Actor(**actor_data)

    str_exc_value = str(exc_info.value)
    assert "skills" in str_exc_value
    assert "Input should be a valid integer" in str_exc_value
