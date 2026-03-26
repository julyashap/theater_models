class IDGenerator:
    """Генератор уникальных идентификаторов."""

    instance = None

    def __new__(cls):
        """Позволяет создать только один экземпляр класса."""
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.counter = 0
        return cls.instance

    def get_id(self) -> int:
        """Возвращает уникальный идентификатор через счетчик."""
        self.counter += 1
        return self.counter
