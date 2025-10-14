class Player:
    """
    Класс игрока в RPG-игре с использованием property
    """

    def __init__(self, name, health=100, level=1, experience=0):
        self._name = name
        self._health = health
        self._level = level
        self._experience = experience

    # Свойство для имени (только для чтения)
    @property
    def name(self):
        return self._name

    # Свойство для здоровья
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
            print(f"{self.name} умер!")
        elif value > 100:
            self._health = 100
            print(f"Здоровье {self.name} полностью восстановлено!")
        else:
            self._health = value

    @health.deleter
    def health(self):
        print(f"Удаление здоровья игрока {self.name}")
        self._health = 0

    # Свойство для уровня
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 1:
            raise ValueError("Уровень не может быть меньше 1")
        self._level = value
        print(f"{self.name} достиг {value} уровня!")

    @level.deleter
    def level(self):
        raise AttributeError("Уровень игрока нельзя удалить")

    # Свойство для опыта
    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        if value < 0:
            raise ValueError("Опыт не может быть отрицательным")

        # Проверяем, достаточно ли опыта для повышения уровня
        exp_for_next_level = self._level * 100
        if value >= exp_for_next_level:
            self._level += 1
            self._experience = value - exp_for_next_level
            print(f"{self.name} повысил уровень до {self._level}!")
        else:
            self._experience = value

    @experience.deleter
    def experience(self):
        print(f"Сброс опыта игрока {self.name}")
        self._experience = 0

    def __str__(self):
        return (f"Игрок {self.name}: "
                f"Здоровье={self.health}, "
                f"Уровень={self.level}, "
                f"Опыт={self.experience}")