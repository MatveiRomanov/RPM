import module1_static_maps
import module2_geocoder
import module3_weather


def main():
    print("🚀 Лабораторная работа №11 - Работа с API")
    print("=" * 50)

    while True:
        print("\n📋 Выберите задание:")
        print("1. Спутниковый снимок БГПУ (Яндекс Карты)")
        print("2. Поиск почтового индекса")
        print("3. Прогноз погоды")
        print("0. Выход")

        choice = input("\nВаш выбор (0-4): ").strip()

        if choice == '1':
            print("\n🛰️  Задание 1: Получение спутникового снимка БГПУ")
            module1_static_maps.get_bgpu_satellite_image()

        elif choice == '2':
            print("\n📮 Задание 2: Поиск почтового индекса")
            address = input("Введите адрес: ")
            module2_geocoder.get_postal_code(address)

        elif choice == '3':
            print("\n🌤️  Задание 3: Прогноз погоды")
            city = input("Введите название города: ")
            module3_weather.get_weather(city)

        elif choice == '0':
            print("👋 До свидания!")
            break

        else:
            print("❌ Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()