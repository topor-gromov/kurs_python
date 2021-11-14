from utils import currency_rates_args
from sys import argv

if len(argv) > 1:
    string_currency = str(argv[1:]).upper()
    str_code_currency = ''
    for letter in string_currency:
        if ord(letter) >= 65 and ord(letter) <= 90:
            str_code_currency = str_code_currency + letter
    currency_rates_args(str_code_currency)
else:
    print('Вы не ввели код валюты в качестве параметра!')