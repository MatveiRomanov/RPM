from vehicles import *
from geometric_shapes import *
from smart_devices import *


def demonstrate_basic_classes():
    print("=" * 50)
    print("ПРИМЕР БАЗОВЫХ КЛАССОВ\n")
    print("=" * 50)

    # WheeledVehicle
    print("1. Транспортное средство:")
    car = WheeledVehicle(180, "бензин", 4)
    print(car.start_engine())
    print(car.check_tires())
    print()

    # CargoTransport
    print("2. Грузовой транспорт:")
    truck = CargoTransport(90, "дизель", 5000)
    print(truck.start_engine())
    print(truck.load_cargo(2000))
    print(truck.load_cargo(4000))  # Перегруз
    print()

    # PassengerTransport
    print("3. Пассажирский транспорт:")
    bus = PassengerTransport(80, "газ", 40)
    print(bus.start_engine())
    print(bus.board_passengers(35))
    print(bus.board_passengers(10))  # Перегруз
    print()

    # EcoFriendlyVehicle
    print("4. Экологичный транспорт:")
    eco_car = EcoFriendlyVehicle(120, "электричество", 0)
    print(eco_car.start_engine())
    print(eco_car.get_eco_info())
    print()


def demonstrate_heavy_duty():
    print("ПРИМЕР ТЯЖЕЛОЙ ТЕХНИКИ\n")

    heavy_truck = HeavyDutyVehicle(
        max_speed=80,
        fuel_type="дизель",
        wheel_count=10,
        cargo_capacity=15000,
        max_weight=25000
    )

    print(heavy_truck.start_engine())
    print(heavy_truck.load_cargo(8000))
    print(heavy_truck.reinforce_frame())
    print(heavy_truck.check_tires())
    print(heavy_truck.get_weight_info())
    print()


def demonstrate_hybrid_van():
    print("ПРИМЕР ГИБРИДНОГО ФУРГОНА\n")

    # гибридный фургон
    delivery_van = HybridDeliveryVan(
        max_speed=120,
        fuel_type="гибрид (бензин/электричество)",
        wheel_count=4,
        cargo_capacity=1500,
        max_weight=3500,
        passenger_capacity=8,
        emission_level=95,
        model="EcoDelivery 3000"
    )

    print("\nНачальный статус:")
    print(delivery_van.status())

    # функциональность
    print("\nФункциональность")
    print(delivery_van.start_engine())
    print(delivery_van.load_cargo(800))
    print(delivery_van.board_passengers(5))
    print(delivery_van.reduce_emission(20))
    print(delivery_van.reinforce_frame())
    print(delivery_van.drive(50))

    print("\nФинальный статус:")
    print(delivery_van.status())


if __name__ == "__main__":
    # Демонстрация транспортных средств (задание 1)
    demonstrate_basic_classes()
    demonstrate_heavy_duty()
    demonstrate_hybrid_van()

    # Демонстрация геометрических фигур (задание 2)
    demonstrate_geometric_shapes()

    # Демонстрация умных устройств (задание 3)
    demonstrate_diamond_problem()
    demonstrate_smart_devices()
