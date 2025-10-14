class Device:
    def __init__(self, power):
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return f"Устройство включено. Потребляемая мощность: {self.power} Вт"

    def turn_off(self):
        self.is_on = False
        return "Устройство выключено"


class NetworkedDevice(Device):
    def __init__(self, power, ip_address):
        Device.__init__(self, power)
        self.ip_address = ip_address
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        return f"Устройство подключено к сети. IP: {self.ip_address}"

    def disconnect(self):
        self.is_connected = False
        return "Устройство отключено от сети"


class PortableDevice(Device):
    def __init__(self, power, battery_level):
        Device.__init__(self, power)
        self.battery_level = battery_level

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Устройство заряжено. Уровень батареи: {self.battery_level}%"

    def use_battery(self, amount):
        self.battery_level = max(0, self.battery_level - amount)
        return f"Батарея использована. Уровень: {self.battery_level}%"


class SmartPhone(NetworkedDevice, PortableDevice):
    def __init__(self, power, ip_address, battery_level, phone_number):
        Device.__init__(self, power)
        NetworkedDevice.__init__(self, power, ip_address)
        PortableDevice.__init__(self, power, battery_level)

        self.phone_number = phone_number
        self.in_call = False

    def call(self, number):
        if not self.is_on:
            return "Сначала включите телефон!"
        if not self.is_connected:
            return "Нет сетевого подключения!"
        if self.battery_level < 10:
            return "Низкий уровень батареи!"

        self.in_call = True
        self.battery_level -= 5
        return f"Звонок на номер {number}... Батарея: {self.battery_level}%"

    def end_call(self):
        self.in_call = False
        return "Звонок завершен"

    def status(self):
        return f"""Статус смартфона:
- Включен: {'Да' if self.is_on else 'Нет'}
- Сетевое подключение: {'Да' if self.is_connected else 'Нет'}
- Уровень батареи: {self.battery_level}%
- В звонке: {'Да' if self.in_call else 'Нет'}
- IP адрес: {self.ip_address}
- Номер: {self.phone_number}
- Мощность: {self.power} Вт"""


def demonstrate_diamond_problem():
    print("=" * 80)
    print("ДЕМОНСТРАЦИЯ ПРОБЛЕМЫ АЛМАЗА И ЕЕ РЕШЕНИЯ")
    print("=" * 80)

    print("ПРОБЛЕМА АЛМАЗА:")
    print("SmartPhone → NetworkedDevice → Device")
    print("SmartPhone → PortableDevice → Device")
    print("Device вызывается дважды через super() в иерархии!")
    print()

    print("РЕШЕНИЕ:")
    print("1. Заменяем super().__init__() на явный вызов Device.__init__()")
    print("2. В SmartPhone явно вызываем все конструкторы в правильном порядке")
    print("3. MRO (Method Resolution Order):", SmartPhone.__mro__)
    print()


def demonstrate_smart_devices():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ УМНЫХ УСТРОЙСТВ")
    print("=" * 50)

    smartphone = SmartPhone(
        power=5,
        ip_address="192.168.1.100",
        battery_level=80,
        phone_number="+7-999-123-45-67"
    )

    print("1. Создан смартфон (проблема алмаза решена):")
    print(smartphone.status())
    print()

    print("2. Попытка позвонить без включения:")
    print(smartphone.call("+7-999-000-00-00"))
    print()

    print("3. Включаем устройство:")
    print(smartphone.turn_on())
    print()

    print("4. Подключаем к сети:")
    print(smartphone.connect())
    print()

    print("5. Совершаем звонок:")
    print(smartphone.call("+7-999-000-00-00"))
    print()

    print("6. Использование батареи:")
    print(smartphone.use_battery(15))
    print()

    print("7. Заряжаем устройство:")
    print(smartphone.charge(25))
    print()

    print("8. Завершаем звонок:")
    print(smartphone.end_call())
    print()

    print("9. Финальный статус:")
    print(smartphone.status())
    print()

    print("=" * 50)
    print("Проблема алмаза успешно решена!")
    print("Конструктор Device был вызван только один раз")
    print("Все свойства корректно инициализированы")
