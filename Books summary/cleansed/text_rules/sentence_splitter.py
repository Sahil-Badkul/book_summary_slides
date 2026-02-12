import re
from .abbreviations import ABBREVIATIONS
from .numbers import protect_numbers, restore_numbers


def protect_abbreviations(text):
    for abbr in ABBREVIATIONS:
        safe = abbr.replace(".", "<DOT>")
        text = text.replace(abbr, safe)
    return text


def restore_abbreviations(text):
    return text.replace("<DOT>", ".")


def split_sentences(text):
    # Step 1 — protect abbreviations
    text = protect_abbreviations(text)

    # Step 2 — protect numbers (1. 2. 3.)
    text = protect_numbers(text)

    # Step 3 — split sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    # Step 4 — restore abbreviations & numbers
    sentences = [restore_numbers(s) for s in sentences]
    sentences = [restore_abbreviations(s) for s in sentences]

    return [s.strip() for s in sentences if s.strip()]
