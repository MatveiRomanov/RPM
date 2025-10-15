import re
from typing import List

def find_repeated_words(text: str) -> List[str]:
    pattern = r'\b(\w+)\s+\1\b'
    matches = re.findall(pattern, text)
    return list(set(matches))  # убираем дубликаты