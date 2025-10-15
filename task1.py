class InterfaceChecker(type):
    def __new__(cls, name, bases, attrs):
        # Проверяем, что класс не является базовым
        if bases and name not in ['BasePlugin', 'CorrectPlugin', 'BrokenPlugin']:
            required_methods = ['load', 'save']
            for method in required_methods:
                if method not in attrs:
                    raise TypeError(f"Класс {name} должен содержать метод {method}")

        return super().__new__(cls, name, bases, attrs)


# Базовый класс с метаклассом
class BasePlugin(metaclass=InterfaceChecker):
    pass


# Корректный класс с нужными методами
class CorrectPlugin(BasePlugin):
    def load(self):
        print("Загрузка данных")

    def save(self):
        print("Сохранение данных")


# Некорректный класс - вызовет ошибку при объявлении
class BrokenPlugin(BasePlugin):
    def load(self):
        print("Только загрузка")
        # Метод save отсутствует - ДОЛЖНА БЫТЬ ОШИБКА