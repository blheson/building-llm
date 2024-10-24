import re

def split_text(text):
    result = re.split(r'([,.()?:;_!"\']|--|\s)',text)
    result = [item.strip() for item in result if item.strip()]
    return result
