from PageSearch import find_passwords_on_webpage
from fileSearch import find_passwords_in_file


find_passwords_on_webpage('https://github.com/kotvisnet/lab_3/tree/master')

print(find_passwords_in_file('passwords.txt'))


