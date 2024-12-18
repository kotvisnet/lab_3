from RegularExpression import is_valid_password

def user_input_check():
    password = input("Enter password: ")

    if not isinstance(password, str):
        raise TypeError("The entered value must be a string.")
    if is_valid_password(password):
        print("Password is correct!")
    else:
        print("Incorrect password.")


if __name__ == "__main__":
    user_input_check()
