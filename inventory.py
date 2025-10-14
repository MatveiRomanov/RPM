class Inventory:
    def __init__(self, weight_limit=100, slots=10):
        self.items = {}
        self.weight_limit = weight_limit
        self.current_weight = 0
        self.slots = slots

    def __str__(self):
        items_str = ", ".join(f"{item}: {count}" for item, count in self.items.items())
        return f"Инвентарь (вместимость: {self.weight_limit}, слоты: {self.slots}): {{{items_str}}}"

    def __iter__(self):
        return iter(self.items.items())

    def __len__(self):
        return sum(self.items.values())

    def __getitem__(self, key):
        return self.items.get(key, 0)

    def __setitem__(self, key, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Количество должно быть неотрицательным целым числом")

        item_weight = 1
        current_count = self.items.get(key, 0)
        weight_change = (value - current_count) * item_weight

        if self.current_weight + weight_change > self.weight_limit:
            raise ValueError("Превышен лимит веса инвентаря")

        if len(self.items) >= self.slots and key not in self.items:
            raise ValueError("Нет свободных слотов")

        self.current_weight += weight_change

        if value == 0 and key in self.items:
            del self.items[key]
        elif value > 0:
            self.items[key] = value

    def __delitem__(self, key):
        if key in self.items:
            item_weight = 1
            self.current_weight -= self.items[key] * item_weight
            del self.items[key]
        else:
            raise KeyError(f"Предмет '{key}' не найден в инвентаре")

    def __contains__(self, item):
        return item in self.items

    def __add__(self, other):
        if not isinstance(other, Inventory):
            raise TypeError("Можно объединять только с другим инвентарем")

        new_weight_limit = max(self.weight_limit, other.weight_limit)
        new_slots = max(self.slots, other.slots)

        new_inventory = Inventory(new_weight_limit, new_slots)

        for item, count in self:
            try:
                new_inventory[item] = count
            except ValueError:
                continue

        for item, count in other:
            try:
                new_inventory[item] = new_inventory[item] + count
            except ValueError:
                continue

        return new_inventory