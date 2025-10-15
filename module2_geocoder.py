import requests


def get_postal_code(address):
    """
    Получает почтовый индекс по адресу используя Yandex Geocoder API
    """
    api_key = '8013b162-6b42-4997-9691-77b7074026e0'

    url = 'https://geocode-maps.yandex.ru/1.x/'

    params = {
        'apikey': api_key,
        'geocode': address,
        'format': 'json',
        'results': 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        # Извлекаем информацию из ответа
        features = data['response']['GeoObjectCollection']['featureMember']

        if not features:
            print("❌ Адрес не найден")
            return None

        geo_object = features[0]['GeoObject']
        postal_code = None

        # Ищем почтовый индекс в метаданных
        if 'metaDataProperty' in geo_object:
            meta_data = geo_object['metaDataProperty']['GeocoderMetaData']
            if 'Address' in meta_data and 'postal_code' in meta_data['Address']:
                postal_code = meta_data['Address']['postal_code']

        if postal_code:
            print(f"📮 Адрес: {address}")
            print(f"📫 Почтовый индекс: {postal_code}")
            return postal_code
        else:
            print(f"❌ Почтовый индекс для адреса '{address}' не найден")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при выполнении запроса: {e}")
        return None
    except KeyError as e:
        print(f"❌ Ошибка при обработке ответа API: {e}")
        return None


if __name__ == "__main__":
    address = input("Введите адрес для поиска почтового индекса: ")
    get_postal_code(address)