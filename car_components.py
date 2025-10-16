class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("Двигатель запущен")

    def stop(self):
        self.running = False
        print("Двигатель остановлен")

    def check_status(self):
        status = "работает" if self.running else "остановлен"
        print(f"Статус двигателя: {status}")


class ClimateControl:
    def __init__(self):
        self.on = False
        self.temperature = 22
        self.fan_speed = 3

    def turn_on(self):
        self.on = True
        print("Климат-контроль включен")

    def turn_off(self):
        self.on = False
        print("Климат-контроль выключен")

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Установлена температура: {temperature}°C")

    def set_fan_speed(self, speed):
        if 1 <= speed <= 5:
            self.fan_speed = speed
            print(f"Установлена скорость вентилятора: {speed}")
        else:
            print("Скорость вентилятора должна быть от 1 до 5")

    def get_status(self):
        status = "включен" if self.on else "выключен"
        return f"Климат-контроль: {status}, температура: {self.temperature}°C, вентилятор: {self.fan_speed}"


class MultimediaSystem:
    def __init__(self):
        self.on = False
        self.volume = 10
        self.current_song = None

    def turn_on(self):
        self.on = True
        print("Мультимедийная система включена")

    def turn_off(self):
        self.on = False
        print("Мультимедийная система выключена")

    def play_music(self, song):
        self.current_song = song
        print(f"Воспроизведение музыки: {song}")

    def set_volume(self, volume):
        if 0 <= volume <= 30:
            self.volume = volume
            print(f"Установлена громкость: {volume}")
        else:
            print("Громкость должна быть от 0 до 30")

    def connect_bluetooth(self):
        print("Bluetooth подключен")

    def get_status(self):
        status = "включена" if self.on else "выключена"
        song_info = f", трек: {self.current_song}" if self.current_song else ""
        return f"Мультимедиа: {status}, громкость: {self.volume}{song_info}"


class Headlights:
    def __init__(self):
        self.on = False
        self.is_high_beam = False

    def turn_on(self):
        self.on = True
        print("Фары включены")

    def turn_off(self):
        self.on = False
        self.is_high_beam = False
        print("Фары выключены")

    def set_high_beam(self):
        if self.on:
            self.is_high_beam = True
            print("Включен дальний свет")
        else:
            print("Сначала включите фары")

    def set_low_beam(self):
        if self.on:
            self.is_high_beam = False
            print("Включен ближний свет")
        else:
            print("Сначала включите фары")

    def get_status(self):
        if not self.on:
            return "Фары: выключены"
        beam_type = "дальний свет" if self.is_high_beam else "ближний свет"
        return f"Фары: включены ({beam_type})"
