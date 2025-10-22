from text_decorators import *
from coffee_system import *
from access_control import *


def demonstrate_text_system():
    print("Система вывода текста\n")

    basic_printer = TextPrinter("Hello World")
    print("1. Базовый текст:", basic_printer.print_text())

    upper_printer = UpperCaseDecorator(basic_printer)
    print("2. Верхний регистр:", upper_printer.print_text())

    border_printer = BorderDecorator(basic_printer)
    print("3. С рамкой:\n", border_printer.print_text())

    exclamation_printer = ExclamationDecorator(basic_printer)
    print("4. С восклицаниями:", exclamation_printer.print_text())

    # Комбинирование декораторов
    combined = BorderDecorator(UpperCaseDecorator(ExclamationDecorator(basic_printer)))
    print("5. Комбинированный:\n", combined.print_text())


def demonstrate_coffee_system():
    print("\nСистема онлайн-заказа кофе\n")

    # Создание базового кофе
    simple_coffee = Coffee()
    print(f"1. {simple_coffee.get_description()}: {simple_coffee.get_cost()} руб.")

    # Кофе с молоком и сахаром
    coffee_with_milk_sugar = SugarDecorator(MilkDecorator(Coffee()))
    print(f"2. {coffee_with_milk_sugar.get_description()}: {coffee_with_milk_sugar.get_cost()} руб.")

    # Кофе со всеми добавками
    premium_coffee = SyrupDecorator(SugarDecorator(MilkDecorator(Coffee())), "шоколадный")
    print(f"3. {premium_coffee.get_description()}: {premium_coffee.get_cost()} руб.")

    # Только сироп
    coffee_with_syrup = SyrupDecorator(Coffee(), "кленовый")
    print(f"4. {coffee_with_syrup.get_description()}: {coffee_with_syrup.get_cost()} руб.")


def demonstrate_access_control():
    print("\nСистема проверки доступа\n")

    admin_user = User(1, "Алексей", "admin")
    regular_user = User(2, "Мария", "user")

    set_current_user(admin_user)
    try:
        result = delete_user(5)
        print(f"1. Администратор: {result}")
    except PermissionError as e:
        print(f"1. Администратор: Ошибка - {e}")

    set_current_user(regular_user)
    try:
        result = delete_user(5)
        print(f"2. Обычный пользователь: {result}")
    except PermissionError as e:
        print(f"2. Обычный пользователь: Ошибка - {e}")

    set_current_user(None)
    try:
        result = delete_user(5)
        print(f"3. Без авторизации: {result}")
    except PermissionError as e:
        print(f"3. Без авторизации: Ошибка - {e}")


def main():
    demonstrate_text_system()
    demonstrate_coffee_system()
    demonstrate_access_control()


if __name__ == "__main__":
    main()
