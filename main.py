from datetime import datetime, time
from pydantic import ValidationError
from models.actor import Actor
from models.viewer import Viewer
from models.production import Production
from models.performance import Performance


def create_valid_viewer() -> Viewer:
    """Создает корректного зрителя."""
    return Viewer(
        name="Anna",
        surname="Ivanova",
        email_address="anna@example.com",
        ticket_number="12345678",
        phone_number="+12345678901",
    )


def create_invalid_viewer() -> None:
    """Создает некорректного зрителя."""
    try:
        Viewer(
            name="A",  # длина < 2
            surname="B",  # длина < 2
            email_address="wrong_email",  # некорректный email
            ticket_number="123",  # длина < 8
            phone_number="89608596"  # некорректный телефон
        )
    except ValidationError as e:
        print("\nViewer ValidationError")
        print(e)


def create_valid_actor() -> Actor:
    """Создает корректного актера."""
    return Actor(
        name="Ivan",
        surname="Petrov",
        passport_number="1234 567890",  # авто-очистка
        skills={
            "diction": 8,
            "vocals": 7,
            "plasticity": 9,
            "tricks": 5  # доп ключ
        },
    )


def create_invalid_actor() -> None:
    """Создает некорректного актера."""
    try:
        Actor(
            name="A",  # длина < 2
            surname="B",  # длина < 2
            passport_number="123",  # длина < 10
            skills={"diction": 5},  # нет обязательных навыков
        )
    except ValidationError as e:
        print("\nActor ValidationError")
        print(e)


def create_valid_production(actor: Actor) -> Production:
    """Создает корректную постановку."""
    return Production(
        name="Hamlet",
        genre="DRAMA",  # преобразование в lowercase
        actors=[actor],
        description="A tragic story about prince Hamlet",
        duration=time(hour=2),
    )


def create_invalid_production(actor: Actor) -> None:
    """Создает некорректную постановку"""
    try:
        Production(
            name="Test",
            genre="comedy",
            actors=[actor, actor],  # дубликаты
        )
    except ValidationError as e:
        print("\nProduction ValidationError")
        print(e)


def create_valid_performance(production: Production, viewer: Viewer) -> Performance:
    """Создает корректное представление."""
    performance = Performance(
        start_datetime=datetime.now(),
        theater_name="Bolshoi",
        count_tickets=100,
        viewers=[viewer],
        production=production,
    )

    return performance


def create_invalid_performance(production: Production, viewer: Viewer) -> None:
    """Создает некорректное представление."""
    try:
        Performance(
            start_datetime=datetime.now(),
            theater_name="Test Theater",
            count_tickets=0,  # = 0
            viewers=[viewer, viewer],  # дубликаты
            production=production,
        )
    except ValidationError as e:
        print("\nPerformance ValidationError")
        print(e)


def main():
    """Точка входа."""
    print("УСПЕШНОЕ ВЫПОЛНЕНИЕ")
    viewer = create_valid_viewer()
    actor = create_valid_actor()
    production = create_valid_production(actor)
    performance = create_valid_performance(production, viewer)

    print(f"\nViewer: {viewer}")
    print(f"\nActor: {actor}")
    print(f"\nProduction: {production}")
    print(f"\nPerformance:\n{performance}")

    print("\nНЕУДАЧНОЕ ВЫПОЛНЕНИЕ")
    create_invalid_actor()
    create_invalid_viewer()
    create_invalid_production(actor)
    create_invalid_performance(production, viewer)


if __name__ == "__main__":
    main()
