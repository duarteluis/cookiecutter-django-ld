import re


def extract_initials_from_name(name: str) -> str:
    """
    Extracts uppercase initials from a full name string.
    Supports Unicode scripts (Latin, Cyrillic, Arabic, etc.).
    Punctuation is stripped except hyphens and apostrophes.

    Args:
        name (str): The full name to extract initials from.

    Returns:
        str: Uppercase initials.
    """
    if not isinstance(name, str) or not name.strip():
        return ""

    cleaned_name = re.sub(r"[^\w\s\-']", " ", name.strip(), flags=re.UNICODE)
    initials = re.findall(r"\b\w", cleaned_name, flags=re.UNICODE)
    return "".join(char.upper() for char in initials)
