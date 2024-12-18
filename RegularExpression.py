import re

""" Пароль должен содержать:
    минимум 8 символов
    минимум одну заглавную букву
    минимум одну строчную букву
    минимум одну цифру
    минимум один специальный символ (например, @, #, $) """

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$"

def is_valid_password(password: str):
    if not isinstance(password, str):
        raise TypeError("password must be str!")
    return re.match(pattern, password) is not None

def find_password_in_text(text: str):
    if not isinstance(text, str):
        raise TypeError("Provided text must be a string.")
    passwords = re.findall(pattern, text)
    return passwords

