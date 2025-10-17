from payment_strategies import CreditCardPayment, EWalletPayment, CashPayment, PaymentContext


def main():
    # Создаем контекст оплаты
    payment_context = PaymentContext()

    print("\nСИСТЕМА ОПЛАТЫ ТОВАРОВ")

    while True:
        print("\nВыберите способ оплаты:")
        print("1. Кредитная карта")
        print("2. Электронный кошелёк")
        print("3. Наличные")
        print("4. Показать историю платежей")
        print("5. Выход")

        choice = input("\nВаш выбор (1-5): ").strip()

        if choice == '5':
            print("До свидания!")
            break

        if choice == '4':
            payment_context.show_payment_history()
            continue

        if choice not in ['1', '2', '3']:
            print("Неверный выбор. Попробуйте снова.")
            continue

        try:
            amount = float(input("Введите сумму оплаты: $"))
            if amount <= 0:
                print("Сумма должна быть положительной!")
                continue
        except ValueError:
            print("Неверный формат суммы!")
            continue

        if choice == '1':
            card_number = input("Введите номер карты: ")
            card_holder = input("Введите имя держателя карты: ")
            expiry_date = input("Введите срок действия (ММ/ГГ): ")
            cvv = input("Введите CVV код: ")

            strategy = CreditCardPayment(card_number, card_holder, expiry_date, cvv)
            payment_context.set_payment_strategy(strategy)

        elif choice == '2':
            wallet_id = input("Введите ID кошелька: ")
            provider = input("Введите провайдера (или Enter для стандартного): ") or "Электронный кошелёк"

            strategy = EWalletPayment(wallet_id, provider)
            payment_context.set_payment_strategy(strategy)

        elif choice == '3':
            strategy = CashPayment()
            payment_context.set_payment_strategy(strategy)

        try:
            result = payment_context.execute_payment(amount)
            print(f"\n{result}")
        except Exception as e:
            print(f"\nОшибка при выполнении платежа: {e}")


if __name__ == "__main__":
    main()