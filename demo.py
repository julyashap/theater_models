from datetime import datetime, time

from src import (
    Actor,
    Performance,
    Production,
    Viewer,
    can_play_role,
    get_cast_list,
    validate_performance,
)


def main():
    """Точка входа."""
    viewer = Viewer(
        name="Anna",
        surname="Ivanova",
        email_address="anna@example.com",
        ticket_number="12345678",
        phone_number="+12345678901",
    )

    actor = Actor(
        name="Ivan",
        surname="Petrov",
        email_address="ivan@example.com",
        passport_number="1234567890",
        skills={"acting": 8, "singing": 7},
    )
    can_actor_play_role = can_play_role(actor, {"acting": 7, "singing": 6})

    production = Production(
        name="Hamlet",
        genre="drama",
        roles={"Hamlet": {"acting": 7, "singing": 6}},
        cast={"Hamlet": actor},
        description="A tragic story about prince Hamlet",
        duration=time(hour=2),
    )
    cast_list = get_cast_list(production)

    performance = Performance(
        start_datetime=datetime.now(),
        theater_name="Bolshoi",
        count_tickets=100,
        viewers=[viewer],
        production=production,
    )
    validate_performance(performance)

    print(f"Viewer\n{viewer}\n")

    print(f"Actor\n{actor}")
    print(f"Can actor {actor.id} play role - {can_actor_play_role}\n")

    print(f"Production\n{production}")
    print(f"Cast list of production {production.id}:\n{cast_list}\n")

    print(f"Performance\n{performance}")


if __name__ == "__main__":
    main()
