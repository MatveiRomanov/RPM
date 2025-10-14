from factorial_recursive import factorial as factorial_recursive
from factorial_cached import factorial as factorial_cached
from custom_cache import factorial as factorial_custom_cache
from logging_decorator import factorial as factorial_logged
from player_class import *


def main():
    #Рекурсивный факториал
    print("\n1. ВЫЧИСЛЕНИЕ ФАКТОРИАЛА РЕКУРСИВНЫМ МЕТОДОМ")
    print("-" * 50)
    numbers = [0, 1, 5, 7, 10]
    for n in numbers:
        result = factorial_recursive(n)
        print(f"Факториал {n}! = {result}")

    #Факториал с встроенным кэшированием
    print("\n2. ФАКТОРИАЛ С ВСТРОЕННЫМ КЭШИРОВАНИЕM")
    print("-" * 50)
    for n in numbers:
        result = factorial_cached(n)
        print(f"Факториал {n}! = {result} (кэшированный)")

    #Факториал с собственным декоратором кэширования
    print("\n3. ФАКТОРИАЛ С СОБСТВЕННЫМ ДЕКОРАТОРОМ КЭШИРОВАНИЯ")
    print("-" * 50)
    for n in numbers:
        result = factorial_custom_cache(n)
        print(f"Факториал {n}! = {result} (собственный кэш)")

    #Факториал с логированием
    print("\n4. ФАКТОРИАЛ С ЛОГИРОВАНИЕМ")
    print("-" * 50)
    try:
        # Успешные вызовы
        factorial_logged(5)
        factorial_logged(3)

        # Вызов с ошибкой
        factorial_logged(-1)
    except ValueError:
        print("Ошибка перехвачена и залогирована")

    #Класс игрока
    print("\n5. КЛАСС ИГРОКА С ИСПОЛЬЗОВАНИЕМ @PROPERTY")
    print("-" * 50)

    # Создаем игрока
    player = Player("Артур", health=80, level=2, experience=150)
    print(f"Создан: {player}")

    # Тестируем свойства
    print("\nТестирование свойств:")

    # Здоровье
    player.health = 120
    print(f"После лечения: {player}")

    player.health = 50
    print(f"После получения урона: {player}")

    player.health = -10
    print(f"После смертельного урона: {player}")

    # Уровень
    player.health = 100
    player.level = 3
    print(f"После повышения уровня: {player}")

    # Опыт
    player.experience = 350
    print(f"После получения опыта: {player}")

    # Тестируем deleter'ы
    print("\nТестирование deleter'ов:")
    del player.health
    print(f"После удаления здоровья: {player}")

    del player.experience
    print(f"После удаления опыта: {player}")

    print("\n" + "=" * 50)
    print("ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ УСПЕШНО!")
    print("=" * 50)


if __name__ == "__main__":
    main()