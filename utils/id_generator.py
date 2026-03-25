class IDGenerator:
    """Генератор уникальных идентификаторов."""

    instance = None
    counter = 0

    def __new__(cls):
        """Позволяет создать только один экземпляр класса."""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def get_id(self) -> int:
        """Возвращает уникальный идентификатор через счетчик."""
        self.counter += 1
        return self.counter
