from ..models.actor import Actor
from ..models.production import Production


def get_missing_roles(production: Production) -> set[str]:
    """Возвращает множество незаполненных ролей."""
    return set(production.roles) - set(production.cast)


def get_cast_list(production: Production) -> list[Actor]:
    """Возвращает список актеров постановки."""
    return list(production.cast.values())


def get_actor_by_role(production: Production, role: str) -> Actor | None:
    """Возвращает актера каста по роли."""
    return production.cast.get(role)
