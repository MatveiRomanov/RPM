from car_components import *


class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.climate_control = ClimateControl()
        self.multimedia_system = MultimediaSystem()
        self.headlights = Headlights()

    def start_car(self):
        print("=== ЗАПУСК АВТОМОБИЛЯ ===")
        self.engine.start()
        self.climate_control.turn_on()
        self.climate_control.set_temperature(22)
        self.climate_control.set_fan_speed(3)
        self.multimedia_system.turn_on()
        self.multimedia_system.connect_bluetooth()
        self.multimedia_system.set_volume(15)
        self.headlights.turn_on()
        self.headlights.set_low_beam()
        print("Автомобиль готов к поездке!\n")

    def stop_car(self):
        print("=== ОСТАНОВКА АВТОМОБИЛЯ ===")
        self.multimedia_system.turn_off()
        self.climate_control.turn_off()
        self.headlights.turn_off()
        self.engine.stop()
        print("Автомобиль остановлен\n")

    def setup_comfort_mode(self):
        print("=== РЕЖИМ КОМФОРТ ===")
        self.climate_control.set_temperature(23)
        self.climate_control.set_fan_speed(2)
        self.multimedia_system.set_volume(12)
        self.multimedia_system.play_music("Расслабляющая музыка")
        print("Режим комфорта активирован\n")

    def setup_night_drive(self):
        print("=== НОЧНАЯ ПОЕЗДКА ===")
        self.headlights.set_high_beam()
        self.climate_control.set_temperature(20)
        self.multimedia_system.set_volume(8)
        self.multimedia_system.play_music("Тихая музыка")
        print("Настройки для ночной поездки применены\n")

    def quick_start(self):
        print("=== БЫСТРЫЙ ЗАПУСК ===")
        self.engine.start()
        self.headlights.turn_on()
        print("Автомобиль готов к движению\n")

    def long_drive(self):
        print("=== ДАЛЬНЯЯ ПОЕЗДКА ===")
        self.start_car()
        self.setup_comfort_mode()
        print("Настройки для дальней поездки применены\n")

    def change_temperature(self, temperature):
        if self.climate_control.on:
            self.climate_control.set_temperature(temperature)
        else:
            print("Сначала включите климат-контроль")

    def change_fan_speed(self, speed):
        if self.climate_control.on:
            self.climate_control.set_fan_speed(speed)
        else:
            print("Сначала включите климат-контроль")

    def change_volume(self, volume):
        if self.multimedia_system.on:
            self.multimedia_system.set_volume(volume)
        else:
            print("Сначала включите мультимедийную систему")

    def play_song(self, song):
        if self.multimedia_system.on:
            self.multimedia_system.play_music(song)
        else:
            print("Сначала включите мультимедийную систему")

    def switch_lights_mode(self, high_beam=False):
        if self.headlights.on:
            if high_beam:
                self.headlights.set_high_beam()
            else:
                self.headlights.set_low_beam()
        else:
            print("Сначала включите фары")

    def get_car_status(self):
        print("=== СТАТУС АВТОМОБИЛЯ ===")
        self.engine.check_status()
        print(self.climate_control.get_status())
        print(self.multimedia_system.get_status())
        print(self.headlights.get_status())
        print()