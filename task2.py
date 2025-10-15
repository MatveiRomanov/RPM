class AutoRegister(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        # Добавляем класс в реестр родительского класса
        if bases:  # Если есть родительские классы
            parent = bases[0]  # Берем первого родителя
            if hasattr(parent, 'registry'):
                parent.registry.append(new_class)

        return new_class


# Базовый класс с метаклассом и реестром
class BaseModel(metaclass=AutoRegister):
    registry = []


# Подклассы автоматически регистрируются
class User(BaseModel):
    pass


class Product(BaseModel):
    pass


# Еще один подкласс
class Order(BaseModel):
    pass