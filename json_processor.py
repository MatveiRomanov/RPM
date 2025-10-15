from data_processor import DataProcessor
from typing import Any
import json


class JSONProcessor(DataProcessor):
    def __init__(self):
        self.data = None

    def load_data(self, source: str) -> None:
        try:
            with open(source, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            print(f"Данные загружены из {source}")
        except FileNotFoundError:
            print(f"Файл {source} не найден")
            self.data = {}
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {source}")
            self.data = {}

    def process_data(self) -> Any:
        if self.data is None:
            return "Данные не загружены"

        if isinstance(self.data, list):
            record_count = len(self.data)
            data_type = "Список"
            if self.data and isinstance(self.data[0], dict):
                keys = list(self.data[0].keys()) if self.data else []
            else:
                keys = []
        elif isinstance(self.data, dict):
            record_count = len(self.data)
            data_type = "Словарь"
            keys = list(self.data.keys())
        else:
            record_count = 1
            data_type = "Простой тип"
            keys = []

        result = {
            'file_type': 'JSON',
            'data_type': data_type,
            'record_count': record_count,
            'keys': keys,
            'sample_data': str(self.data)[:100] + "..." if len(str(self.data)) > 100 else str(self.data)
        }
        return result

    def save_data(self, destination: str) -> None:
        if self.data is None:
            print("Нет данных для сохранения")
            return

        processed_data = self.process_data()

        result_data = {
            "статистика_файла": {
                "тип_файла": processed_data['file_type'],
                "структура_данных": processed_data['data_type'],
                "количество_записей": processed_data['record_count'],
                "ключи_поля": processed_data['keys'],
                "пример_данных": processed_data['sample_data']
            }
        }

        with open(destination, 'w', encoding='utf-8') as file:
            json.dump(result_data, file, ensure_ascii=False, indent=2)

        print(f"Результаты сохранены в {destination}")