import re

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"

def is_valid_password(password: str):
    if not isinstance(password, str):
        raise TypeError("password must be str!")
    return re.match(pattern, password) is not None

def find_password_in_text(text: str):
    if not isinstance(text, str):
        raise TypeError("The provided text must be a string.")
    passwords = re.findall(pattern, text)
    return passwords

