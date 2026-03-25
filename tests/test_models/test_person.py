import pytest

from src.models.person import Person


@pytest.fixture
def person_data() -> dict[str, int | str]:
    """"""
    return {
        "id": 1,
        "name": "  Name  ",
        "surname": "Surname",
        "email_address": "example@mail.com",
        "phone_number": "+79171985623",
    }


def test_valid_person_all_fields(person_data: dict[str, int | str]) -> None:
    """"""
    person = Person(**person_data)

    assert person.id == 1
    assert person.name == "Name"
    assert person.surname == "Surname"


def test_valid_person_default_fields(person_data: dict[str, int | str]) -> None:
    """"""
    person_data.pop("id")
    person_data.pop("phone_number")

    person = Person(**person_data)

    assert person.id == 1
    assert person.phone_number == ""


def test_invalid_person_required_fields(person_data: dict[str, int | str]) -> None:
    """"""
    person_data.pop("name")

    with pytest.raises(ValueError) as exc_info:  
        Person(**person_data) 
    
    str_exc_value = str(exc_info.value)
    assert "name" in str_exc_value
    assert "Field required" in str_exc_value


def test_invalid_person_display_name(person_data: dict[str, int | str]) -> None:
    """"""
    person_data["name"] = ""
    person_data["surname"] = ""

    with pytest.raises(ValueError) as exc_info:  
        Person(**person_data) 
    
    str_exc_value = str(exc_info.value)
    assert "name" in str_exc_value
    assert "surname" in str_exc_value
    assert "String should have at least 1 character" in str_exc_value


def test_invalid_person_email_address(person_data: dict[str, int | str]) -> None:
    """"""
    person_data["email_address"] = "invalid_email"

    with pytest.raises(ValueError) as exc_info:  
        Person(**person_data) 
    
    str_exc_value = str(exc_info.value)
    assert "email_address" in str_exc_value
    assert "value is not a valid email address" in str_exc_value


def test_invalid_person_phone_number(person_data: dict[str, int | str]) -> None:
    """"""
    person_data["phone_number"] = "123456"

    with pytest.raises(ValueError) as exc_info:
        Person(**person_data)

    str_exc_value = str(exc_info.value)
    assert "phone_number" in str_exc_value
    assert "String should match pattern" in str_exc_value
