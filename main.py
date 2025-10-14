from game_items import HealthPotion, ManaCrystal
from bank_accounts import SavingsAccount, CheckingAccount
from employees import Manager, Developer


def task1_demo():
    print("=== Задача 1: Игровые предметы ===")

    potion = HealthPotion("Большой флакон", 0.5, "Обычное")
    crystal = ManaCrystal("Синий осколок", 0.3, "Редкое")

    print(potion.use())
    print(crystal.use())
    print()


def task2_demo():
    print("=== Задача 2: Банковские счета ===")

    savings = SavingsAccount("12345", "Иван", 10000)
    checking = CheckingAccount("67890", "Анна", 5000)

    print(savings.get_account_info())
    print(checking.get_account_info())

    # Демонстрация операций
    print(savings.deposit(1000))
    print(savings.withdraw(2000))
    print()


def task3_demo():
    print("=== Задача 3: Сотрудники компании ===")

    employees = [
        Manager("Иван", 5000, "Менеджер"),
        Developer("Анна", 5000, "Разработчик"),
        Manager("Петр", 6000, "Старший менеджер"),
        Developer("Мария", 5500, "Ведущий разработчик")
    ]

    for employee in employees:
        print(employee.get_info() + ". " + employee.work())

    # Демонстрация повышения
    print("\n--- Повышение сотрудника ---")
    employees[0].promote(1000)
    print(employees[0].get_info())


if __name__ == "__main__":
    task1_demo()
    task2_demo()
    task3_demo()