from point import Point
from typed_array import TypedArray
from task_manager import TaskManager


def demo_point():
    print("=== Демонстрация класса Point ===")

    # Точка с целочисленными координатами
    point_int = Point(1, 2, 3)
    print(f"Point с int: {point_int}")

    # Точка с вещественными координатами
    point_float = Point(1.5, 2.7, 3.9)
    print(f"Point с float: {point_float}")

    print()


def demo_typed_array():
    print("=== Демонстрация класса TypedArray ===")

    # Массив целых чисел
    int_array = TypedArray[int]()
    int_array.add(10)
    int_array.add(20)
    int_array.add(30)
    print(f"Массив int: {int_array}")
    print(f"Элемент с индексом 1: {int_array.get(1)}")

    # Массив строк
    str_array = TypedArray[str]()
    str_array.add("Hello")
    str_array.add("World")
    print(f"Массив str: {str_array}")

    # Обработка ошибки
    try:
        int_array.get(10)  # Неверный индекс
    except IndexError as e:
        print(f"Ошибка: {e}")

    print()


def demo_task_manager():
    print("=== Демонстрация класса TaskManager ===")

    # Менеджер задач с int, str, int
    manager1 = TaskManager[int, str, int]()
    manager1.add_task(1, "Задача 1", 5)
    manager1.add_task(2, "Задача 2", 8)
    manager1.add_task(3, "Задача 3", 3)
    print("Менеджер 1 (int, str, int):")
    print(manager1)
    highest1 = manager1.get_highest_priority_task()
    print(f"Самая приоритетная задача: ID: {highest1[0]}, Описание: {highest1[1]}, Приоритет: {highest1[2]}")

    print()

    # Менеджер задач с str, str, bool
    manager2 = TaskManager[str, str, bool]()
    manager2.add_task("task_a", "Важная задача", True)
    manager2.add_task("task_b", "Обычная задача", False)
    manager2.add_task("task_c", "Срочная задача", True)
    print("Менеджер 2 (str, str, bool):")
    print(manager2)
    highest2 = manager2.get_highest_priority_task()
    print(f"Самая приоритетная задача: ID: {highest2[0]}, Описание: {highest2[1]}, Приоритет: {highest2[2]}")

    print()


if __name__ == "__main__":
    demo_point()
    demo_typed_array()
    demo_task_manager()

    print("Все демонстрации завершены!")