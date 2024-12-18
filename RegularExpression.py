import re

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"

def is_valid_card(card: str):
    if not isinstance(card, str):
        raise TypeError("card must be str!")
    return re.match(pattern, card) is not None

def find_card_in_text(text: str):
    if not isinstance(text, str):
        raise TypeError("The provided text must be a string.")
    cards = re.findall(pattern, text)
    return cards