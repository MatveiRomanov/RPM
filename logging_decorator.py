import time
import functools
from datetime import datetime


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Засекаем время начала выполнения
        start_time = time.time()

        try:
            # Вызываем функцию
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time

            # Логируем успешный вызов
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
                  f" Функция: {func.__name__}"
                  f" | Аргументы: {args} {kwargs}"
                  f" | Результат: {result}"
                  f" | Время выполнения: {execution_time:.6f} сек"
                  f" | Статус: УСПЕХ")

            return result

        except Exception as e:
            execution_time = time.time() - start_time

            # Логируем ошибку
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]"
                  f" Функция: {func.__name__}"
                  f" | Аргументы: {args} {kwargs}"
                  f" | Ошибка: {str(e)}"
                  f" | Время выполнения: {execution_time:.6f} сек"
                  f" | Статус: ОШИБКА")

            # Пробрасываем исключение дальше
            raise

    return wrapper


# Пример использования с факториалом
@log
def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)