import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,6}$'
    return bool(re.match(pattern, email))