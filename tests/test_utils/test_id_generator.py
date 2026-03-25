from src.utils.id_generator import IDGenerator


def test_one_instance() -> None:
    """"""
    id_generator = IDGenerator()

    id_generator_2 = IDGenerator()

    assert id_generator is id_generator_2


def test_get_id_counter() -> None:
    """"""
    id_generator = IDGenerator()

    for i in range(5):
        expected_id = i + 1

        assert id_generator.get_id() == expected_id
