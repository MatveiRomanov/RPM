class MathUtils:
    PI = 3.14159
    E = 2.71828

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Ошибка: деление на ноль!"
        return a / b

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def circle_area(radius):
        return MathUtils.PI * radius ** 2

    @staticmethod
    def is_even(number):
        return number % 2 == 0