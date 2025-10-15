from task1 import CorrectPlugin
from task2 import BaseModel


def run_task1():
    print("=== Задание 1: Контроль структуры классов ===")

    # Создаем экземпляр корректного класса
    correct = CorrectPlugin()
    print("✓ CorrectPlugin создан успешно")
    correct.load()
    correct.save()

    print("\nПопытка создать BrokenPlugin...")
    # Пытаемся создать BrokenPlugin динамически, чтобы поймать ошибку
    try:
        # Имитируем создание класса с отсутствующим методом save
        class TempPlugin(CorrectPlugin):
            def load(self):
                print("Только загрузка")
            # Метод save отсутствует

        temp = TempPlugin()
        print("✗ Ошибка: класс создан без метода save!")
    except TypeError as e:
        print(f"✓ Правильно поймана ошибка: {e}")


def run_task2():
    print("\n=== Задание 2: Автоматическая регистрация подклассов ===")

    print("Содержимое реестра BaseModel.registry:")
    for i, cls in enumerate(BaseModel.registry, 1):
        print(f"{i}. {cls.__name__}")


if __name__ == "__main__":
    run_task1()
    run_task2()