from data_processor import DataProcessor
from typing import Any
import csv


class CSVProcessor(DataProcessor):
    def __init__(self):
        self.data = None

    def load_data(self, source: str) -> None:
        try:
            with open(source, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.data = list(reader)
            print(f"Данные загружены из {source}")
        except FileNotFoundError:
            print(f"Файл {source} не найден")
            self.data = []

    def process_data(self) -> Any:
        if self.data is None:
            return "Данные не загружены"

        record_count = len(self.data) - 1 if self.data else 0  # минус заголовок
        column_count = len(self.data[0]) if self.data else 0

        result = {
            'file_type': 'CSV',
            'record_count': record_count,
            'column_count': column_count,
            'headers': self.data[0] if self.data else [],
            'first_records': self.data[1:4] if len(self.data) > 1 else []
        }
        return result

    def save_data(self, destination: str) -> None:
        if self.data is None:
            print("Нет данных для сохранения")
            return

        processed_data = self.process_data()

        with open(destination, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Статистика CSV файла'])
            writer.writerow(['Тип файла', processed_data['file_type']])
            writer.writerow(['Количество записей', processed_data['record_count']])
            writer.writerow(['Количество столбцов', processed_data['column_count']])
            writer.writerow(['Заголовки', ', '.join(processed_data['headers'])])
            writer.writerow(['Первые записи:'])
            for record in processed_data['first_records']:
                writer.writerow(record)

        print(f"Результаты сохранены в {destination}")