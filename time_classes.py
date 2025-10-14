class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds

        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def __str__(self):
        parts = []
        if self.hours > 0:
            parts.append(f"{self.hours}ч")
        if self.minutes > 0:
            parts.append(f"{self.minutes}м")
        if self.seconds > 0:
            parts.append(f"{self.seconds}с")

        return " ".join(parts) if parts else "0с"

    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        if not isinstance(other, Time):
            raise TypeError("Можно складывать только с объектом Time")

        total_sec = self.total_seconds() + other.total_seconds()

        hours = total_sec // 3600
        minutes = (total_sec % 3600) // 60
        seconds = total_sec % 60

        return Time(hours, minutes, seconds)

    def __sub__(self, other):
        if not isinstance(other, Time):
            raise TypeError("Можно вычитать только объект Time")

        total_sec = self.total_seconds() - other.total_seconds()

        if total_sec < 0:
            return Time(0, 0, 0)

        hours = total_sec // 3600
        minutes = (total_sec % 3600) // 60
        seconds = total_sec % 60

        return Time(hours, minutes, seconds)

    def __eq__(self, other):
        if not isinstance(other, Time):
            return False
        return self.total_seconds() == other.total_seconds()

class Seconds:
    def __init__(self, seconds=0):
        self.seconds = int(seconds)

    def __str__(self):
        return f"{self.seconds}с"

    def __int__(self):
        return self.seconds


class Minutes:
    def __init__(self, minutes=0):
        self.minutes = int(minutes)

    def __str__(self):
        return f"{self.minutes}м"

    def __int__(self):
        return self.minutes


class Hours:
    def __init__(self, hours=0):
        self.hours = int(hours)

    def __str__(self):
        return f"{self.hours}ч"

    def __int__(self):
        return self.hours