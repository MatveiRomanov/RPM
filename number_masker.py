import re

def mask_numbers(text: str) -> str:
    pattern = r'\b\d+(?:\.\d+)?\b'
    return re.sub(pattern, '<num>', text)