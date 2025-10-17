from vehicle_system import *


def main():
    print("=== Система управления транспортными средствами ===\n")

    # Создаем различные двигатели
    gasoline_engine = GasolineEngine()
    electric_engine = ElectricEngine()
    hybrid_engine = HybridEngine()

    # Создаем транспортные средства с разными двигателями
    gasoline_car = Car(gasoline_engine)
    electric_car = Car(electric_engine)
    hybrid_bike = Bike(hybrid_engine)
    electric_bike = Bike(electric_engine)

    # Демонстрируем работу системы
    vehicles = [gasoline_car, electric_car, hybrid_bike, electric_bike]

    for vehicle in vehicles:
        print(f"Транспорт: {vehicle.__class__.__name__}")
        print(f"Двигатель: {vehicle.engine.__class__.__name__}")
        print(vehicle.start_engine())
        print(vehicle.drive())
        print(vehicle.stop_engine())
        print("-" * 50)


if __name__ == "__main__":
    main()