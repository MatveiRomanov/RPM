from task1 import task1_demo
from task2 import task2_demo
from task3 import task3_demo


def main():
    print("Лабораторная работа №8: Дата-классы")
    print("=" * 50)

    # Задание 1
    books = task1_demo()

    # Задание 2
    persons = task2_demo()

    # Задание 3
    order = task3_demo()

    print("\n" + "=" * 50)
    print("Все задания выполнены успешно!")


if __name__ == "__main__":
    main()