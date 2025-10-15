import re


def is_strong_password(password: str) -> bool:
    if len(password) < 8 or len(password) > 20:
        return False

    checks = [
        r'[A-Z]',  # заглавные буквы
        r'[a-z]',  # строчные буквы
        r'\d',  # цифры
        r'[@#$%^&+=]'  # спецсимволы
    ]

    return all(re.search(pattern, password) for pattern in checks)