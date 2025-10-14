from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, base_rate, position):
        self.name = name
        self.base_rate = base_rate
        self.position = position

    def get_info(self):
        salary = self.calculate_salary()
        return f"Сотрудник: {self.name} ({self.position}). Зарплата: {salary}"

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def work(self):
        pass

    def promote(self, increase_amount):
        self.base_rate += increase_amount
        return f"{self.name} получил повышение! Новая базовая ставка: {self.base_rate}"


class Manager(Employee):
    def calculate_salary(self):
        return self.base_rate * 1.5

    def work(self):
        return "Организует работу команды"


class Developer(Employee):
    def calculate_salary(self):
        return self.base_rate + 500

    def work(self):
        return "Пишет код и исправляет ошибки"