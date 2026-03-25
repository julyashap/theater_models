import pytest

from src.models.viewer import Viewer


@pytest.fixture
def viewer_data() -> dict[str, int | str]:
    """"""
    return {
        "id": 1,
        "name": "Name",
        "surname": "Surname",
        "email_address": "example@mail.com",
        "phone_number": "+79171985623",
        "ticket_number": "12345678",
    }


def test_valid_viewer_all_fields(viewer_data: dict[str, int | str]) -> None:
    """"""
    viewer = Viewer(**viewer_data)

    assert viewer.id == 1
    assert viewer.name == "Name"
    assert viewer.surname == "Surname"
    assert viewer.ticket_number == "12345678"


def test_invalid_viewer_ticket_number_pattern(viewer_data: dict[str, int | str]) -> None:
    """"""
    viewer_data["ticket_number"] = "1234ABCD"

    with pytest.raises(ValueError) as exc_info:
        Viewer(**viewer_data)

    str_exc_value = str(exc_info.value)
    assert "ticket_number" in str_exc_value
    assert "String should match pattern" in str_exc_value
