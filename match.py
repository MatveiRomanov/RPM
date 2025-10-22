from observer_pattern import *


class Match(Subject):
    def __init__(self, team1: str, team2: str):
        super().__init__()
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0

    def set_score(self, score1: int, score2: int):
        self.score1 = score1
        self.score2 = score2
        self.notify()  # Уведомляем всех наблюдателей об изменении счета

    def get_score(self) -> str:
        return f"{self.team1} {self.score1} - {self.score2} {self.team2}"

    def __str__(self):
        return self.get_score()


class Scoreboard(Observer):
    def update(self, match: Match):
        print(f"[ТАБЛО] Обновление счета: {match.get_score()}")


class MobileApp(Observer):
    def __init__(self, user_name: str):
        self.user_name = user_name

    def update(self, match: Match):
        print(f"[МОБИЛЬНОЕ ПРИЛОЖЕНИЕ] Уведомление для {self.user_name}: "
              f"Счет изменился! {match.get_score()}")


class Commentator(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, match: Match):
        print(f"[КОММЕНТАТОР {self.name.upper()}] "
              f"Внимание! Счет изменился: {match.get_score()}")

        # Комментатор добавляет свой комментарий
        if match.score1 > match.score2:
            print(f"    '{match.team1} ведет в счете!'")
        elif match.score1 < match.score2:
            print(f"    '{match.team2} выходит вперед!'")
        else:
            print(f"    'Ничья! Напряженная борьба!'")