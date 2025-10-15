from data_processor import DataProcessor
from typing import Any


class TXTProcessor(DataProcessor):
    def __init__(self):
        self.data = None

    def load_data(self, source: str) -> None:
        try:
            with open(source, 'r', encoding='utf-8') as file:
                self.data = file.readlines()
            print(f"Данные загружены из {source}")
        except FileNotFoundError:
            print(f"Файл {source} не найден")
            self.data = []

    def process_data(self) -> Any:
        if self.data is None:
            return "Данные не загружены"

        line_count = len(self.data)
        word_count = sum(len(line.split()) for line in self.data)

        result = {
            'file_type': 'TXT',
            'line_count': line_count,
            'word_count': word_count,
            'content_preview': self.data[:3] if self.data else []
        }
        return result

    def save_data(self, destination: str) -> None:
        if self.data is None:
            print("Нет данных для сохранения")
            return

        processed_data = self.process_data()

        with open(destination, 'w', encoding='utf-8') as file:
            file.write(f"Статистика TXT файла:\n")
            file.write(f"Количество строк: {processed_data['line_count']}\n")
            file.write(f"Количество слов: {processed_data['word_count']}\n")
            file.write(f"Первые 3 строки:\n")
            for line in processed_data['content_preview']:
                file.write(f"  {line.strip()}\n")

        print(f"Результаты сохранены в {destination}")