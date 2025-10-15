import requests



def get_bgpu_satellite_image():
    """
    Получает спутниковый снимок БГПУ используя Yandex Static Maps API
    """

    # Пробуем разные подходы, так как API ключ может быть нерабочим

    # Способ 1: Используем публичный API Яндекс Карт (не требует ключа)
    def method_public_api():
        # Координаты БГПУ (Благовещенский государственный педагогический университет)
        longitude = 127.527
        latitude = 50.259

        params = {
            'll': f'{longitude},{latitude}',
            'z': '16',
            'l': 'sat',  # Спутниковый режим
            'size': '650,450'
        }

        url = 'https://static-maps.yandex.ru/1.x/'

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

            with open('bgpu_satellite.jpg', 'wb') as f:
                f.write(response.content)

            print("✅ Спутниковый снимок БГПУ успешно сохранен как 'bgpu_satellite.jpg'")
            return True

        except requests.exceptions.RequestException as e:
            print(f"❌ Ошибка при получении изображения: {e}")
            return False

    # Способ 2: Пробуем с оригинальным API ключом (на случай если он рабочий)
    def method_with_key():
        api_key = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        longitude = 127.527
        latitude = 50.259

        params = {
            'apikey': api_key,
            'll': f'{longitude},{latitude}',
            'z': '16',
            'l': 'sat',
            'size': '650,450'
        }

        url = 'https://static-maps.yandex.ru/1.x/'

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

            with open('bgpu_satellite_key.jpg', 'wb') as f:
                f.write(response.content)

            print("✅ Спутниковый снимок БГПУ с API ключом сохранен как 'bgpu_satellite_key.jpg'")
            return True

        except requests.exceptions.RequestException as e:
            print(f"❌ Ошибка при получении изображения с API ключом: {e}")
            return False

    print("🛰️  Пытаемся получить спутниковый снимок БГПУ...")

    # Пробуем сначала публичный API
    if method_public_api():
        return

    # Если не получилось, пробуем с ключом
    print("\n🔄 Пробуем альтернативный метод...")
    method_with_key()


if __name__ == "__main__":
    get_bgpu_satellite_image()