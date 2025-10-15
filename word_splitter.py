import re
from typing import List

def split_words(text: str) -> List[str]:
    pattern = r'\b\w+\b'
    return re.findall(pattern, text)