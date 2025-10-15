import requests


def get_weather(city_name):
    """
    Получает текущую погоду для указанного города используя OpenWeatherMap API
    """
    api_key = "bd5e378503939ddaee76f12ad7a97608"  # Бесплатный ключ для демонстрации

    url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # Градусы Цельсия
        'lang': 'ru'  # Русский язык
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        # Извлекаем данные о погоде
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print(f"🌍 Погода в {city}, {country}:")
        print(f"🌡️  Температура: {temp}°C (ощущается как {feels_like}°C)")
        print(f"📝 Описание: {description.capitalize()}")
        print(f"💧 Влажность: {humidity}%")
        print(f"📊 Давление: {pressure} гПа")
        print(f"💨 Скорость ветра: {wind_speed} м/с")

        return data

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при получении данных о погоде: {e}")
        return None
    except KeyError as e:
        print(f"❌ Ошибка при обработке данных: {e}")
        return None


if __name__ == "__main__":
    city = input("Введите название города: ")
    get_weather(city)