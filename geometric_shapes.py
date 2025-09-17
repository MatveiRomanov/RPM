import math


class Shape:
    def area(self):
        raise NotImplementedError("Метод area() должен быть реализован в подклассе")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть реализован в подклассе")

    def __str__(self):
        return f"{self.__class__.__name__}: площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}"


class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Формула Герона
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class RightTriangle(Triangle):
    def __init__(self, a, b):
        # a и b - катеты
        c = math.sqrt(a ** 2 + b ** 2)  # гипотенуза
        super().__init__(a, b, c)
        self.cathetus_a = a
        self.cathetus_b = b
        self.hypotenuse = c


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.side = side


def demonstrate_geometric_shapes():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ ГЕОМЕТРИЧЕСКИХ ФИГУР (ЗАДАНИЕ 2)")
    print("=" * 50)

    # Создание различных фигур
    figures = [
        Circle(5),
        Rectangle(4, 6),
        Square(5),
        Triangle(3, 4, 5),
        RightTriangle(3, 4),
        EquilateralTriangle(6)
    ]

    # Вывод информации о каждой фигуре
    for i, figure in enumerate(figures, 1):
        print(f"{i}. {figure}")

        # Дополнительная информация для некоторых фигур
        if isinstance(figure, Rectangle):
            print(f"   Диагональ: {figure.diagonal():.2f}")
        elif isinstance(figure, RightTriangle):
            print(f"   Гипотенуза: {figure.hypotenuse:.2f}")

