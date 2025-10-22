class Coffee:
    def __init__(self):
        self._description = "Простой кофе"
        self._cost = 100

    def get_cost(self):
        return self._cost

    def get_description(self):
        return self._description


class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee


class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 50

    def get_description(self):
        return self._coffee.get_description() + ", молоко"


class SugarDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 20

    def get_description(self):
        return self._coffee.get_description() + ", сахар"


class SyrupDecorator(CoffeeDecorator):
    def __init__(self, coffee, syrup_type="ванильный"):
        super().__init__(coffee)
        self._syrup_type = syrup_type

    def get_cost(self):
        return self._coffee.get_cost() + 70

    def get_description(self):
        return self._coffee.get_description() + f", {self._syrup_type} сироп"
