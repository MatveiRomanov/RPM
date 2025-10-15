from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


class Product(ABC):
    @abstractmethod
    def get_total_price(self) -> float:
        pass


@dataclass
class Item(Product):
    name: str
    price: float
    quantity: int

    def get_total_price(self) -> float:
        return self.price * self.quantity


@dataclass
class Order:
    items: List[Item] = field(default_factory=list)

    def total_sum(self) -> float:
        return sum(item.get_total_price() for item in self.items)

    def add_item(self, item: Item):
        self.items.append(item)

    def get_items_sorted_by_price_desc(self) -> List[Item]:
        return sorted(self.items, key=lambda item: item.price, reverse=True)


def task3_demo():
    print("\n=== Задание 3: Система заказов ===")

    # Создаем товары
    items = [
        Item("Ноутбук", 50000.0, 1),
        Item("Мышь", 1500.0, 2),
        Item("Клавиатура", 3000.0, 1),
        Item("Монитор", 25000.0, 1),
        Item("Наушники", 5000.0, 1)
    ]

    # Создаем заказ и добавляем товары
    order = Order()
    for item in items:
        order.add_item(item)

    print("Товары в заказе:")
    for item in order.items:
        print(f"  {item.name}: {item.price} руб. × {item.quantity} = {item.get_total_price()} руб.")

    print(f"\nОбщая сумма заказа: {order.total_sum()} руб.")

    print("\nТовары отсортированы по убыванию цены:")
    sorted_items = order.get_items_sorted_by_price_desc()
    for item in sorted_items:
        print(f"  {item.name}: {item.price} руб.")

    return order