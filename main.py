from car_facade import CarFacade


def demonstrate_car_facade():
    car = CarFacade()

    print("ДЕМОНСТРАЦИЯ РАБОТЫ ФАСАДА АВТОМОБИЛЯ")
    print("=" * 50 + "\n")

    print("1. ПОЛНЫЙ ЗАПУСК АВТОМОБИЛЯ:")
    car.start_car()

    print("2. ИНДИВИДУАЛЬНОЕ УПРАВЛЕНИЕ СИСТЕМАМИ:")
    print("- Изменение температуры:")
    car.change_temperature(25)

    print("- Изменение громкости:")
    car.change_volume(18)

    print("- Смена музыки:")
    car.play_song("Любимый плейлист")

    print("- Переключение на дальний свет:")
    car.switch_lights_mode(high_beam=True)

    car.get_car_status()

    print("3. НАСТРОЙКА РЕЖИМА КОМФОРТА:")
    car.setup_comfort_mode()

    print("4. НАСТРОЙКА НОЧНОЙ ПОЕЗДКИ:")
    car.setup_night_drive()

    print("5. ОСТАНОВКА АВТОМОБИЛЯ:")
    car.stop_car()

    print("6. ГОТОВЫЕ СЦЕНАРИИ ПОЕЗДОК:")
    print("-" * 30)

    print("Сценарий: Дальняя поездка")
    car.long_drive()

    print("Индивидуальные настройки во время поездки:")
    car.change_temperature(21)
    car.change_fan_speed(4)
    car.play_song("Дорожная музыка")

    car.get_car_status()
    car.stop_car()

    print("Сценарий: Быстрый запуск")
    car.quick_start()
    car.stop_car()


def interactive_mode():
    car = CarFacade()

    print("\nИНТЕРАКТИВНЫЙ РЕЖИМ УПРАВЛЕНИЯ АВТОМОБИЛЕМ")
    print("=" * 50)

    while True:
        print("\nВыберите действие:")
        print("1 - Полный запуск автомобиля")
        print("2 - Быстрый запуск")
        print("3 - Дальняя поездка")
        print("4 - Ночная поездка")
        print("5 - Режим комфорта")
        print("6 - Остановить автомобиль")
        print("7 - Показать статус")
        print("\n--- ИНДИВИДУАЛЬНОЕ УПРАВЛЕНИЕ ---")
        print("8 - Изменить температуру")
        print("9 - Изменить скорость вентилятора")
        print("10 - Изменить громкость")
        print("11 - Включить музыку")
        print("12 - Переключить фары (ближний/дальний)")
        print("0 - Выход")

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            car.start_car()
        elif choice == "2":
            car.quick_start()
        elif choice == "3":
            car.long_drive()
        elif choice == "4":
            car.setup_night_drive()
        elif choice == "5":
            car.setup_comfort_mode()
        elif choice == "6":
            car.stop_car()
        elif choice == "7":
            car.get_car_status()
        elif choice == "8":
            if car.climate_control.on:
                temp = int(input("Введите температуру (16-30): "))
                car.change_temperature(temp)
            else:
                print("Сначала включите климат-контроль")
        elif choice == "9":
            if car.climate_control.on:
                speed = int(input("Введите скорость вентилятора (1-5): "))
                car.change_fan_speed(speed)
            else:
                print("Сначала включите климат-контроль")
        elif choice == "10":
            if car.multimedia_system.on:
                volume = int(input("Введите громкость (0-30): "))
                car.change_volume(volume)
            else:
                print("Сначала включите мультимедийную систему")
        elif choice == "11":
            if car.multimedia_system.on:
                song = input("Введите название трека: ")
                car.play_song(song)
            else:
                print("Сначала включите мультимедийную систему")
        elif choice == "12":
            if car.headlights.on:
                mode = input("Режим (1-ближний, 2-дальний): ")
                car.switch_lights_mode(mode == "2")
            else:
                print("Сначала включите фары")
        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    demonstrate_car_facade()
    interactive_mode()