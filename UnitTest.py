import unittest
from unittest.mock import patch, mock_open
import requests
from RegularExpression import is_valid_password, find_password_in_text
from PageSearch import find_passwords_on_webpage
from fileSearch import find_passwords_in_file

class TestRepassword(unittest.TestCase):
    def test_is_valid_password(self):
        self.assertTrue(is_valid_password("Password: Qw10-iujh6 ~"))
        self.assertTrue(is_valid_password("Password: 1Omdn+1sx ~"))
        self.assertFalse(is_valid_password("Password: polina123 ~"))
        self.assertFalse(is_valid_password("Password: m1m1m1m ~"))
        self.assertFalse(is_valid_password("Password: password ~"))

    def test_find_passwords_in_text(self):
        text = "Password: Qw10-iujh6 ~ 8998ugyv10293939"
        result = find_password_in_text(text)
        self.assertEqual(result, ["Password: Qw10-iujh6 ~"])


class TestFilepasswordSearch(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="Password: 1Omdn+1sx ~\nPassword: 111111 ~")
    def test_find_passwords_in_file(self, mock_file):
        result = find_passwords_in_file('passwords.txt')
        self.assertEqual(result, ["Password: 1Omdn+1sx ~"])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_find_passwords_in_file_not_found(self, mock_file):
        with patch("builtins.print") as mock_print:
            find_passwords_in_file("password.txt")
            mock_print.assert_called_with(
                "Error: The file was not found. Make sure that the path is specified correctly.")

class TestPagepasswordSearch(unittest.TestCase):
    @patch("requests.get")
    def test_find_passwords_on_webpage(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Password: PolRos-1358! ~"

        with patch("builtins.print") as mock_print:
            find_passwords_on_webpage("https://github.com/kotvisnet/lab_3/tree/master")
            mock_print.assert_called_with("Found passwords on the page:", {'Password: PolRos-1358! ~'})

    @patch("requests.get")
    def test_find_passwords_on_webpage_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")

        with patch("builtins.print") as mock_print:
            find_passwords_on_webpage("https://github.com/kotvisnet")
            mock_print.assert_called_with("An unexpected error occurred: Network error")


if __name__ == "__main__":
    unittest.main()