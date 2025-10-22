from fibonacci_iterator import *


def demonstrate_fibonacci():
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ИТЕРАТОРА И ГЕНЕРАТОРА ЧИСЕЛ ФИБОНАЧЧИ")

    print("\n1. Использование итератора:")

    fib_iter = FibonacciIterator(10)
    print("Первые 10 чисел Фибоначчи (итератор):")
    for num in fib_iter:
        print(num, end=" ")
    print()

    print("\n2. Использование генератора (yield):")

    fib_gen = fibonacci_generator(10)
    print("Первые 10 чисел Фибоначчи (генератор):")
    for num in fib_gen:
        print(num, end=" ")
    print()

    print("\n3. Сравнение результатов:")

    iter_nums = list(FibonacciIterator(15))
    gen_nums = list(fibonacci_generator(15))

    print(f"Результаты идентичны: {iter_nums == gen_nums}")
    print(f"Количество элементов: {len(iter_nums)}")

    print("\nПодробное сравнение первых 15 чисел:")
    print("№  | Итератор | Генератор")
    print("-" * 25)
    for i, (iter_val, gen_val) in enumerate(zip(iter_nums, gen_nums)):
        print(f"{i + 1:2} | {iter_val:8} | {gen_val:8}")


def demonstrate_manual_iteration():
    print("\n\n4. Ручная итерация:")

    fib_iter = FibonacciIterator(5)

    print("Ручной вызов next():")
    try:
        while True:
            print(next(fib_iter), end=" ")
    except StopIteration:
        print("\nИтерация завершена!")


if __name__ == "__main__":
    demonstrate_fibonacci()
    demonstrate_manual_iteration()
