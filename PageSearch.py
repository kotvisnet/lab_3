import requests
from RegularExpression import find_password_in_text, pattern
import re


def find_passwords_on_webpage(url):
    try:
        if not isinstance(url, str):
            raise TypeError("The URL must be a string.")

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        text = response.text
        pattern = r'Password: (?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=_-]).{8,} ~'
        if not isinstance(text, str):
            raise TypeError("Provided text must be a string.")
        passwords = re.findall(pattern, text)

        if passwords:
            print("Found passwords on the page:", set(passwords))
        else:
            print("No passwords addresses were found on the page.")

    except requests.Timeout:
        print("Error: The request timed out. Please check your connection or try a different URL.")
    except requests.ConnectionError:
        print("Error: Unable to connect to the server. Please check your internet connection.")
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except TypeError as e:
        print(f"Type error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the web page: ")
    find_passwords_on_webpage(url)