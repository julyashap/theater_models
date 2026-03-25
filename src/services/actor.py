from models.actor import Actor
from models.type_aliases import Skills


def can_play_role(actor: Actor, required_skills: Skills) -> bool:
    """Проверяет, сможет ли актер сыграть роль."""
    for skill, required_level in required_skills.items():
        if actor.skills.get(skill, 0) < required_level:
            return False
    return True


def filter_actors_for_role(actors: list[Actor], required_skills: Skills) -> list[Actor]:
    """Фильтрует актеров по необходимым для роли навыкам."""
    return [
        actor for actor in actors
        if can_play_role(actor, required_skills)
    ]
