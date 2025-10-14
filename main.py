from math_utils import *
from student_registry import *


def demo_math_utils():
    print("=== Демонстрация MathUtils ===")

    # Демонстрация констант
    print(f"PI = {MathUtils.PI}")
    print(f"E = {MathUtils.E}")

    # Демонстрация математических операций
    print(f"5 + 3 = {MathUtils.add(5, 3)}")
    print(f"10 - 4 = {MathUtils.subtract(10, 4)}")
    print(f"6 * 7 = {MathUtils.multiply(6, 7)}")
    print(f"15 / 3 = {MathUtils.divide(15, 3)}")
    print(f"8 / 0 = {MathUtils.divide(8, 0)}")
    print(f"2^8 = {MathUtils.power(2, 8)}")
    print(f"Площадь круга с радиусом 5: {MathUtils.circle_area(5):.2f}")
    print(f"8 четное? {MathUtils.is_even(8)}")
    print(f"7 четное? {MathUtils.is_even(7)}")
    print()


def demo_student_registry():
    print("=== Демонстрация StudentRegistry ===")

    # Добавление студентов
    StudentRegistry.add_student("Иван Иванов")
    StudentRegistry.add_student("Петр Петров")
    StudentRegistry.add_student("Мария Сидорова")

    # Получение информации о студентах
    print(f"Количество студентов: {StudentRegistry.get_student_count()}")
    print(f"Список студентов: {StudentRegistry.get_all_students()}")

    # Добавление еще одного студента
    StudentRegistry.add_student("Анна Козлова")
    print(f"Обновленное количество студентов: {StudentRegistry.get_student_count()}")
    print(f"Обновленный список студентов: {StudentRegistry.get_all_students()}")

    # Очистка реестра
    StudentRegistry.clear_registry()
    print(f"Количество студентов после очистки: {StudentRegistry.get_student_count()}")
    print(f"Список студентов после очистки: {StudentRegistry.get_all_students()}")


if __name__ == "__main__":
    demo_math_utils()
    demo_student_registry()