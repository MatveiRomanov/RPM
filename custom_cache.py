def cache(func):
    cache_dict = {}

    def wrapper(n):
        if n not in cache_dict:
            cache_dict[n] = func(n)
        return cache_dict[n]

    # Для очистки кэша
    wrapper.clear_cache = lambda: cache_dict.clear()

    return wrapper


@cache
def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)