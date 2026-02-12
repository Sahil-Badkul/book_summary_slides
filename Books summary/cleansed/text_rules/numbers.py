import re

def protect_numbers(text):
    # Replace patterns like "1." → "1<DOT>"
    return re.sub(r'(\d+)\.', r'\1<DOT>', text)

def restore_numbers(text):
    return text.replace("<DOT>", ".")
