from datetime import datetime, timedelta
from typing import Any

import pytest

from src.models.actor import Actor
from src.models.performance import Performance
from src.models.production import Production
from src.models.type_aliases import Skills
from src.models.viewer import Viewer


@pytest.fixture
def viewer_sample() -> Viewer:
    """Простой объект Viewer."""
    return Viewer(
        id=1,
        name="Alice",
        surname="Smith",
        email_address="alice@mail.com",
        phone_number="+79171112233",
        ticket_number="12345678",
    )


@pytest.fixture
def performance_data(production_sample: Production) -> dict[str, Any]:
    """Данные для создания Performance."""
    return {
        "id": 1,
        "start_datetime": datetime.now() + timedelta(days=1),
        "theater_name": "Grand Theater",
        "count_tickets": 5,
        "production": production_sample,
        "is_premiere": True,
    }


def test_valid_performance_all_fields(performance_data: dict[str, Any]) -> None:
    """Проверяет создание модели при корректных данных."""
    performance = Performance(**performance_data)

    assert performance.id == 1
    assert performance.theater_name == "Grand Theater"
    assert performance.available_tickets == 5
    assert performance.is_premiere is True
    assert performance.viewers == []


def test_add_viewer_success(
    performance_data: dict[str, Any], viewer_sample: Viewer
) -> None:
    """Проверяет успешное добавление зрителя."""
    performance = Performance(**performance_data)

    performance.add_viewer(viewer_sample)

    assert len(performance.viewers) == 1
    assert performance.viewers[0].id == viewer_sample.id
    assert performance.available_tickets == 4


def test_add_viewers_success(
    performance_data: dict[str, Any], viewer_sample: Viewer
) -> None:
    """Проверяет успешное добавление нескольких зрителей."""
    performance = Performance(**performance_data)
    viewer_2 = Viewer(
        id=2,
        name="Bob",
        surname="Brown",
        email_address="bob@mail.com",
        phone_number="+79172223344",
        ticket_number="87654321",
    )

    performance.add_viewers([viewer_sample, viewer_2])

    assert len(performance.viewers) == 2
    assert performance.available_tickets == 3


def test_add_viewer_exceed_tickets(performance_data: dict[str, Any]) -> None:
    """Проверяет выброс ошибки при переполнении зрителей при добавлении."""
    performance = Performance(**performance_data)
    for i in range(5):
        performance.add_viewer(
            Viewer(
                name=f"V{i}",
                surname="Test",
                email_address=f"v{i}@mail.com",
                phone_number=f"+7900000000{i}",
                ticket_number=f"{10000000+i}",
            )
        )

    extra_viewer = Viewer(
        name="Extra",
        surname="Viewer",
        email_address="extra@mail.com",
        phone_number="+79179998877",
        ticket_number="99999999",
    )

    with pytest.raises(ValueError) as exc_info:
        performance.add_viewer(extra_viewer)

    assert "doesn't fit, no tickets available" in str(exc_info.value)


def test_add_viewer_duplicate(
    performance_data: dict[str, Any], viewer_sample: Viewer
) -> None:
    """Проверяет выброс ошибки при повторном добавлении того же зрителя."""
    performance = Performance(**performance_data)
    performance.add_viewer(viewer_sample)

    with pytest.raises(ValueError) as exc_info:
        performance.add_viewer(viewer_sample)

    assert "already exists in Performance" in str(exc_info.value)


def test_unique_viewers_validation(performance_data: dict[str, Any]) -> None:
    """Проверяет выброс ошибки при неуникальном списке зрителей."""
    viewer_1 = Viewer(
        id=1,
        name="Alice",
        surname="Smith",
        email_address="alice@mail.com",
        phone_number="+79171112233",
        ticket_number="12345678",
    )
    viewer_2 = Viewer(
        id=1,
        name="Alice2",
        surname="Smith2",
        email_address="alice2@mail.com",
        phone_number="+79171112234",
        ticket_number="12345679",
    )
    performance_data["viewers"] = [viewer_1, viewer_2]

    with pytest.raises(ValueError) as exc_info:
        Performance(**performance_data)

    assert "Viewers must be unique" in str(exc_info.value)


def test_count_viewers_not_exceed_tickets(performance_data: dict[str, Any]) -> None:
    """Проверяет выброс ошибки при переполнении зрителей при создании."""
    viewers = [
        Viewer(
            name=f"V{i}",
            surname="Test",
            email_address=f"v{i}@mail.com",
            phone_number=f"+7900000000{i}",
            ticket_number=f"{10000000+i}",
        )
        for i in range(6)
    ]
    performance_data["viewers"] = viewers

    with pytest.raises(ValueError) as exc_info:
        Performance(**performance_data)

    assert "Count viewers must be less or equal than count tickets" in str(
        exc_info.value
    )


def test_available_tickets(
    performance_data: dict[str, Any], viewer_sample: Viewer
) -> None:
    """Проверяет корректность работы вычисляемого поля."""
    performance = Performance(**performance_data)
    assert performance.available_tickets == 5

    performance.add_viewer(viewer_sample)
    assert performance.available_tickets == 4
