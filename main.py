from csv_processor import CSVProcessor
from json_processor import JSONProcessor
from txt_processor import TXTProcessor


def main():
    print("=== Лабораторная работа №7: Интерфейсы в Python ===\n")

    # Создаем объекты процессоров
    csv_processor = CSVProcessor()
    json_processor = JSONProcessor()
    txt_processor = TXTProcessor()

    # Демонстрация работы с CSV файлом
    print("1. Обработка CSV файла:")
    csv_processor.load_data("data.csv")
    csv_result = csv_processor.process_data()
    print(f"Результат обработки: {csv_result}")
    csv_processor.save_data("csv_results.csv")
    print()

    # Демонстрация работы с JSON файлом
    print("2. Обработка JSON файла:")
    json_processor.load_data("data.json")
    json_result = json_processor.process_data()
    print(f"Результат обработки: {json_result}")
    json_processor.save_data("json_results.json")
    print()

    # Демонстрация работы с TXT файлом
    print("3. Обработка TXT файла:")
    txt_processor.load_data("data.txt")
    txt_result = txt_processor.process_data()
    print(f"Результат обработки: {txt_result}")
    txt_processor.save_data("txt_results.txt")
    print()

    print("Обработка завершена!")


if __name__ == "__main__":
    main()