from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Пополнение на {amount}. Новый баланс: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Снятие {amount}. Новый баланс: {self.balance}"
        else:
            return "Недостаточно средств на счете"

    @abstractmethod
    def calculate_interest(self):
        pass

    def get_account_info(self):
        interest = self.calculate_interest()
        return f"Счет №{self.account_number} (Владелец: {self.owner}). Баланс: {self.balance}. Проценты: {interest}"


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.05


class CheckingAccount(BankAccount):
    def calculate_interest(self):
        return 0