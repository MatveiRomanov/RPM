from match import *


def main():
    match = Match("Реал Мадрид", "Барселона")

    scoreboard = Scoreboard()
    mobile_app_user1 = MobileApp("Иван Петров")
    mobile_app_user2 = MobileApp("Мария Сидорова")
    commentator = Commentator("Сергей Иванов")

    match.attach(scoreboard)
    match.attach(mobile_app_user1)
    match.attach(mobile_app_user2)
    match.attach(commentator)

    print("НАЧАЛО МАТЧА")
    print(f"Матч: {match.team1} vs {match.team2}")
    print()

    print("МИНУТА 15: ГОООЛ!")
    match.set_score(1, 0)
    print()

    print("МИНУТА 33: ГОООЛ!")
    match.set_score(1, 1)
    print()

    print("МИНУТА 67: ГОООЛ!")
    match.set_score(2, 1)
    print()

    print("МИНУТА 89: ГОООЛ!")
    match.set_score(2, 2)
    print()

    print("Мария Сидорова отключила уведомления")
    match.detach(mobile_app_user2)
    print()

    print("МИНУТА 90+3: ГОООЛ!")
    match.set_score(3, 2)
    print()

    print("КОНЕЦ МАТЧА")
    print(f"ФИНАЛЬНЫЙ СЧЕТ: {match.get_score()}")


if __name__ == "__main__":
    main()