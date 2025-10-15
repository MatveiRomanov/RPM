from email_validator import is_valid_email
from date_extractor import extract_dates
from number_masker import mask_numbers
from password_checker import is_strong_password
from html_tag_extractor import extract_tags
from word_repetition_finder import find_repeated_words
from word_splitter import split_words


def main():
    print("=== Лабораторная работа №10: Регулярные выражения ===\n")

    # Тестирование задания 1
    print("1. Валидация email-адреса:")
    test_emails = ["john_doe@example.com", "user.name@domain.co.uk", "invalid@email"]
    for email in test_emails:
        print(f"   {email}: {is_valid_email(email)}")

    # Тестирование задания 2
    print("\n2. Извлечение дат:")
    text = "Встреча 12-04-2023 и потом 15/05/2024"
    print(f"   Текст: {text}")
    print(f"   Даты: {extract_dates(text)}")

    # Тестирование задания 3
    print("\n3. Замена чисел:")
    text = "У него было 5 яблок и 3.14 пирога"
    print(f"   Исходный: {text}")
    print(f"   Результат: {mask_numbers(text)}")

    # Тестирование задания 4
    print("\n4. Проверка пароля:")
    passwords = ["StrongPass1!", "weak", "NoDigit!", "Short1!"]
    for pwd in passwords:
        print(f"   '{pwd}': {is_strong_password(pwd)}")

    # Тестирование задания 5
    print("\n5. Поиск HTML-тегов:")
    html = "<div><p>Hello</p><br/></div>"
    print(f"   HTML: {html}")
    print(f"   Теги: {extract_tags(html)}")

    # Тестирование задания 6
    print("\n6. Поиск повторяющихся слов:")
    text = "This is is a test test test string"
    print(f"   Текст: {text}")
    print(f"   Повторы: {find_repeated_words(text)}")

    # Тестирование задания 7
    print("\n7. Разделение строки по словам:")
    text = "Hello, world! How are you?"
    print(f"   Текст: {text}")
    print(f"   Слова: {split_words(text)}")


if __name__ == "__main__":
    main()