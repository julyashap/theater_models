from src.theater.utils.id_generator import IDGenerator


def test_single_instance() -> None:
    """Проверяет создание единственного экземпляра."""
    id_generator = IDGenerator()

    id_generator_2 = IDGenerator()

    assert id_generator is id_generator_2


def test_counter_instance_attribute() -> None:
    """Проверяет, что поле counter является атрибутом экземпляра."""
    id_generator = IDGenerator()

    assert not hasattr(IDGenerator, "counter")
    assert id_generator.counter == 0


def test_get_id_counter() -> None:
    """Проверяет корректность работы счетчика."""
    id_generator = IDGenerator()

    for i in range(5):
        expected_id = i + 1

        assert id_generator.get_id() == expected_id
