import re
from typing import List

def extract_tags(html: str) -> List[str]:
    pattern = r'</?(\w+)[^>]*>'
    return re.findall(pattern, html)