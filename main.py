from inventory import *
from time_classes import *


def demo_inventory():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ КЛАССА INVENTORY")
    print("=" * 50)

    # Создаем инвентарь с большей вместимостью
    inv1 = Inventory(weight_limit=100, slots=10)
    print("Создан инвентарь 1:", inv1)

    # Добавляем предметы
    inv1["меч"] = 1
    inv1["зелье"] = 3
    inv1["стрела"] = 20
    print("После добавления предметов:", inv1)
    print(f"Текущий вес: {inv1.current_weight}/{inv1.weight_limit}")

    # Проверяем доступ к предметам
    print(f"\nКоличество зелий: {inv1['зелье']}")
    print(f"Есть ли меч в инвентаре: {'меч' in inv1}")
    print(f"Есть ли щит в инвентаре: {'щит' in inv1}")
    print(f"Общее количество предметов: {len(inv1)}")

    # Итерируемся по инвентарю
    print("\nПредметы в инвентаре:")
    for item, count in inv1:
        print(f"  {item}: {count}")

    # Создаем второй инвентарь
    inv2 = Inventory(weight_limit=80, slots=8)
    inv2["щит"] = 1
    inv2["зелье"] = 2
    inv2["золото"] = 30
    print(f"\nСоздан инвентарь 2: {inv2}")
    print(f"Текущий вес инвентаря 2: {inv2.current_weight}/{inv2.weight_limit}")

    # Объединяем инвентари
    print("\n--- ОБЪЕДИНЕНИЕ ИНВЕНТАРЕЙ ---")
    combined_inv = inv1 + inv2
    print("Объединенный инвентарь:", combined_inv)
    print(f"Текущий вес объединенного инвентаря: {combined_inv.current_weight}/{combined_inv.weight_limit}")

    # Удаляем предмет
    print("\n--- УДАЛЕНИЕ ПРЕДМЕТА ---")
    print("До удаления стрел:", combined_inv)
    del combined_inv["стрела"]
    print("После удаления стрел:", combined_inv)
    print(f"Текущий вес после удаления: {combined_inv.current_weight}/{combined_inv.weight_limit}")


def demo_time():
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ КЛАССОВ ВРЕМЕНИ")
    print("=" * 50)

    # Демонстрация отдельных классов
    print("--- ОТДЕЛЬНЫЕ КЛАССЫ ---")
    sec = Seconds(45)
    min = Minutes(30)
    hour = Hours(2)

    print(f"Секунды: {sec}")
    print(f"Минуты: {min}")
    print(f"Часы: {hour}")
    print(f"Целое значение секунд: {int(sec)}")
    print(f"Целое значение минут: {int(min)}")
    print(f"Целое значение часов: {int(hour)}")

    # Демонстрация класса Time
    print("\n--- КЛАСС TIME ---")

    # Создаем объекты времени разными способами
    time1 = Time(hours=2, minutes=30, seconds=45)
    time2 = Time(hours=1, minutes=15, seconds=20)
    time3 = Time(minutes=45, seconds=10)
    time4 = Time(seconds=120)
    time5 = Time()  # Пустое время

    print(f"Время 1 (2ч 30м 45с): {time1}")
    print(f"Время 2 (1ч 15м 20с): {time2}")
    print(f"Время 3 (45м 10с): {time3}")
    print(f"Время 4 (120с): {time4}")
    print(f"Время 5 (пустое): {time5}")

    # Демонстрация автоматического преобразования
    print(f"\n--- АВТОМАТИЧЕСКОЕ ПРЕОБРАЗОВАНИЕ ---")
    time6 = Time(minutes=65, seconds=70)  # 65 минут 70 секунд = 1ч 6м 10с
    time7 = Time(seconds=3665)  # 3665 секунд = 1ч 1м 5с
    time8 = Time(hours=1, minutes=90, seconds=150)  # 1 час 90 минут 150 секунд = 2ч 31м 30с

    print(f"Время 6 (65м 70с): {time6}")
    print(f"Время 7 (3665с): {time7}")
    print(f"Время 8 (1ч 90м 150с): {time8}")

    # Демонстрация total_seconds()
    print(f"\n--- ОБЩЕЕ ВРЕМЯ В СЕКУНДАХ ---")
    print(f"Время 1 в секундах: {time1.total_seconds()}")
    print(f"Время 2 в секундах: {time2.total_seconds()}")
    print(f"Время 6 в секундах: {time6.total_seconds()}")
    print(f"Время 7 в секундах: {time7.total_seconds()}")

    # Демонстрация сложения
    print(f"\n--- СЛОЖЕНИЕ ВРЕМЕНИ ---")
    time_sum = time1 + time2
    print(f"Время 1 + Время 2 = {time_sum}")

    time_sum2 = time2 + time6
    print(f"Время 2 + Время 6 = {time_sum2}")

    # Демонстрация вычитания
    print(f"\n--- ВЫЧИТАНИЕ ВРЕМЕНИ ---")
    time_diff = time1 - time2
    print(f"Время 1 - Время 2 = {time_diff}")

    time_diff2 = time6 - time2
    print(f"Время 6 - Время 2 = {time_diff2}")

    # Демонстрация сравнения (ИСПРАВЛЕННАЯ)
    print(f"\n--- СРАВНЕНИЕ ВРЕМЕНИ ---")
    time9 = Time(minutes=65, seconds=70)  # 1ч 6м 10с
    time10 = Time(hours=1, minutes=6, seconds=10)  # 1ч 6м 10с

    print(f"Время 1 равно Время 2: {time1 == time2}")
    print(f"Время 6 (65м 70с): {time6.total_seconds()} секунд")
    print(f"Время 7 (3665с): {time7.total_seconds()} секунд")
    print(f"Время 6 равно Время 7: {time6 == time7}")
    print(f"Время 9 равно Время 10: {time9 == time10}")  # Должно быть True

    # Демонстрация одинакового времени
    print(f"\n--- ПРОВЕРКА ИДЕНТИЧНОСТИ ---")
    time11 = Time(hours=1, minutes=30)
    time12 = Time(minutes=90)
    time13 = Time(seconds=5400)

    print(f"Время 11 (1ч 30м): {time11} = {time11.total_seconds()}с")
    print(f"Время 12 (90м): {time12} = {time12.total_seconds()}с")
    print(f"Время 13 (5400с): {time13} = {time13.total_seconds()}с")
    print(f"Все три времени равны: {time11 == time12 == time13}")


if __name__ == "__main__":
    demo_inventory()
    demo_time()