from models.performance import Performance


def validate_performance(performance: Performance) -> None:
    """Валидирует представление через постановку."""
    performance.production.validate_cast()
