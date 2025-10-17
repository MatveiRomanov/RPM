from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class GasolineEngine(Engine):
    def start(self):
        return "Бензиновый двигатель запущен"

    def stop(self):
        return "Бензиновый двигатель остановлен"


class ElectricEngine(Engine):
    def start(self):
        return "Электрический двигатель запущен"

    def stop(self):
        return "Электрический двигатель остановлен"


class HybridEngine(Engine):
    def start(self):
        return "Гибридный двигатель запущен"

    def stop(self):
        return "Гибридный двигатель остановлен"


class Vehicle(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def drive(self):
        pass

    def start_engine(self):
        return self.engine.start()

    def stop_engine(self):
        return self.engine.stop()


class Car(Vehicle):
    def drive(self):
        return f"{self.engine.start().lower()}"


class Bike(Vehicle):
    def drive(self):
        return f"{self.engine.start().lower()}"

