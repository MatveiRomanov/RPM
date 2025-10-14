from abc import ABC, abstractmethod


class GameItem(ABC):
    def __init__(self, item_name, weight, rarity):
        self.item_name = item_name
        self.weight = weight
        self.rarity = rarity

    def get_description(self):
        return f"{self.item_name} (Редкость: {self.rarity}, Вес: {self.weight})"

    @abstractmethod
    def use(self):
        pass


class HealthPotion(GameItem):
    def get_description(self):
        return f'Зелье здоровья "{self.item_name}" (Редкость: {self.rarity}, Вес: {self.weight})'

    def use(self):
        return f"{self.get_description()} использовано: +50 HP"


class ManaCrystal(GameItem):
    def get_description(self):
        return f'Кристалл маны "{self.item_name}" (Редкость: {self.rarity}, Вес: {self.weight})'

    def use(self):
        return f"{self.get_description()} использован: +30 MP"