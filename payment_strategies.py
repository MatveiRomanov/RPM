from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder, expiry_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Обработка оплаты кредитной картой...")
        print(f"Карта: **** **** **** {self.card_number[-4:]}")
        print(f"Держатель: {self.card_holder}")
        print(f"Сумма: ${amount:.2f}")
        print("Проверка безопасности... Успешно!")
        print("Средства списаны с карты.")
        return f"Оплата кредитной картой на сумму ${amount:.2f} прошла успешно"


class EWalletPayment(PaymentStrategy):
    def __init__(self, wallet_id, provider="Электронный кошелёк"):
        self.wallet_id = wallet_id
        self.provider = provider

    def pay(self, amount):
        print(f"Обработка {self.provider} платежа...")
        print(f"Кошелёк: {self.wallet_id}")
        print(f"Сумма: ${amount:.2f}")
        print("Подтверждение транзакции... Успешно!")
        print("Баланс кошелька обновлён.")
        return f"Электронный платёж на сумму ${amount:.2f} выполнен успешно"


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print("Обработка наличного платежа...")
        print(f"Сумма к оплате: ${amount:.2f}")
        print("Ожидание внесения наличных...")
        print("Наличные приняты. Сдача выдана.")
        print("Чек распечатан.")
        return f"Наличный платёж на сумму ${amount:.2f} завершён"


class PaymentContext:
    def __init__(self, payment_strategy=None):
        self._payment_strategy = payment_strategy
        self.payment_history = []

    def set_payment_strategy(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def execute_payment(self, amount):
        if not self._payment_strategy:
            raise ValueError("Стратегия оплаты не установлена")

        print("\nНАЧАЛО ТРАНЗАКЦИИ")

        result = self._payment_strategy.pay(amount)

        transaction = {
            'amount': amount,
            'strategy': type(self._payment_strategy).__name__,
            'result': result,
            'timestamp': '2024-01-15 14:30:00'
        }
        self.payment_history.append(transaction)

        print("\nТРАНЗАКЦИЯ ЗАВЕРШЕНА")

        return result

    def show_payment_history(self):
        if not self.payment_history:
            print("История платежей пуста")
            return

        print("\n" + "=" * 60)
        print("ИСТОРИЯ ПЛАТЕЖЕЙ")
        print("=" * 60)
        for i, transaction in enumerate(self.payment_history, 1):
            print(f"{i}. {transaction['strategy']} - ${transaction['amount']:.2f}")
            print(f"   Результат: {transaction['result']}")
            print(f"   Время: {transaction['timestamp']}")
            print("-" * 40)