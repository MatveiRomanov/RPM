class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self.engine_started = False
        print(f"Созданно ТС: {max_speed} км/ч, {fuel_type}")

    def start_engine(self):
        if not self.engine_started:
            self.engine_started = True
            return f"Двигатель запущен. Тип топлива: {self.fuel_type}"
        return "Двигатель уже запущен"

    def stop_engine(self):
        if self.engine_started:
            self.engine_started = False
            return "Двигатель остановлен"
        return "Двигатель уже остановлен"



class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, **kwargs):
        # Вызываем конструктор родительского класса
        super().__init__(max_speed, fuel_type, **kwargs)
        self.wheel_count = wheel_count
        print(f"Инициализирован WheeledVehicle: {wheel_count} колес")

    def check_tires(self):
        return f"Проверка {self.wheel_count} колес завершена. Все в норме."


class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity, **kwargs):
        super().__init__(max_speed, fuel_type, **kwargs)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0
        print(f"Инициализирован CargoTransport: грузоподъемность {cargo_capacity} кг")

    def load_cargo(self, weight):
        if self.current_cargo + weight <= self.cargo_capacity:
            self.current_cargo += weight
            return f"Груз загружен. Текущий груз: {self.current_cargo}/{self.cargo_capacity} кг"
        return f"Перегруз! Максимум: {self.cargo_capacity} кг"

    def unload_cargo(self, weight=None):
        if weight is None:
            weight = self.current_cargo

        if weight <= self.current_cargo:
            self.current_cargo -= weight
            return f"Груз разгружен. Осталось: {self.current_cargo} кг"
        return "Нельзя разгрузить больше чем есть"


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity, **kwargs):
        super().__init__(max_speed, fuel_type, **kwargs)
        self.passenger_capacity = passenger_capacity
        self.current_passengers = 0
        print(f"Инициализирован PassengerTransport: вместимость {passenger_capacity} пасс.")

    def board_passengers(self, count):
        if self.current_passengers + count <= self.passenger_capacity:
            self.current_passengers += count
            return f"Пассажиры размещены. Текущее количество: {self.current_passengers}/{self.passenger_capacity}"
        return f"Недостаточно мест! Максимум: {self.passenger_capacity}"

    def disembark_passengers(self, count=None):
        if count is None:
            count = self.current_passengers

        if count <= self.current_passengers:
            self.current_passengers -= count
            return f"Пассажиры высажены. Осталось: {self.current_passengers}"
        return "Нельзя высадить больше пассажиров чем есть"


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level, **kwargs):
        super().__init__(max_speed, fuel_type, **kwargs)
        self.emission_level = emission_level
        print(f"Инициализирован EcoFriendlyVehicle: выбросы {emission_level} г/км")

    def reduce_emission(self, reduction):
        if self.emission_level - reduction >= 0:
            self.emission_level -= reduction
            return f"Выбросы снижены до {self.emission_level} г/км"
        return "Уровень выбросов не может быть отрицательным"

    def get_eco_info(self):
        return f"Уровень выбросов: {self.emission_level} г/км"


class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight, **kwargs):
        # Используем super() с MRO
        super().__init__(
            max_speed=max_speed,
            fuel_type=fuel_type,
            wheel_count=wheel_count,
            cargo_capacity=cargo_capacity,
            **kwargs
        )
        self.max_weight = max_weight
        self.frame_reinforced = False
        print(f"Инициализирован HeavyDutyVehicle: макс. вес {max_weight} кг")

    def reinforce_frame(self):
        self.frame_reinforced = True
        return "Рама усилена. Готов к тяжелым грузам!"

    def get_weight_info(self):
        return f"Макс. вес: {self.max_weight} кг, Грузоподъемность: {self.cargo_capacity} кг"


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity,
                 max_weight, passenger_capacity, emission_level, model):
        print(f"\nСоздание HybridDeliveryVan: {model}")

        # Используем super() с передачей всех параметров
        super().__init__(
            max_speed=max_speed,
            fuel_type=fuel_type,
            wheel_count=wheel_count,
            cargo_capacity=cargo_capacity,
            max_weight=max_weight,
            passenger_capacity=passenger_capacity,
            emission_level=emission_level
        )

        # Специфические атрибуты фургона
        self.model = model
        self.odometer = 0  # Пробег
        print(f"Инициализирован HybridDeliveryVan: модель {model}")

    def status(self):
        status_info = [
            f"Статус фургона {self.model}",
            f"Макс. скорость: {self.max_speed} км/ч",
            f"Топливо: {self.fuel_type}",
            f"Колеса: {self.wheel_count} шт.",
            f"Груз: {self.current_cargo}/{self.cargo_capacity} кг",
            f"Пассажиры: {self.current_passengers}/{self.passenger_capacity}",
            f"Выбросы: {self.emission_level} г/км",
            f"Макс. вес: {self.max_weight} кг",
            f"Двигатель: {'запущен' if self.engine_started else 'остановлен'}",
            f"Рама усилена: {'да' if self.frame_reinforced else 'нет'}",
            f"Пробег: {self.odometer} км",
        ]
        return "\n".join(status_info)

    def drive(self, distance):
        if self.engine_started:
            self.odometer += distance
            return f"Проехали {distance} км. Общий пробег: {self.odometer} км"
        return "Сначала запустите двигатель!"
