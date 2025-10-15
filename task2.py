from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Person(ABC):
    @abstractmethod
    def full_name(self) -> str:
        pass

    @abstractmethod
    def get_id(self) -> str:
        pass


@dataclass
class Student(Person):
    first_name: str
    last_name: str
    student_id: str

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_id(self) -> str:
        return f"Student ID: {self.student_id}"


@dataclass
class Teacher(Person):
    first_name: str
    last_name: str
    employee_id: str
    courses: List[str]

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_id(self) -> str:
        return f"Employee ID: {self.employee_id}"


def print_persons_info(persons: List[Person]):
    for person in persons:
        print(f"{person.full_name()} - {person.get_id()}")


def task2_demo():
    students = [
        Student("Иван", "Петров", "S001"),
        Student("Мария", "Сидорова", "S002"),
        Student("Алексей", "Иванов", "S003")
    ]

    teachers = [
        Teacher("Ольга", "Смирнова", "T001", ["Математика", "Физика"]),
        Teacher("Дмитрий", "Козлов", "T002", ["Информатика", "Программирование"]),
        Teacher("Елена", "Васильева", "T003", ["Литература", "Русский язык"])
    ]

    all_persons = students + teachers

    print("\n=== Задание 2: Студенты и преподаватели ===")
    print_persons_info(all_persons)

    return all_persons