from requests import get
from decimal import getcontext, Decimal

def currency_rates(currency_code):
    # приводим введённый результат к верхнему регистру и формируем строку запроса.
    start_str = '<CharCode>' + str(currency_code).upper() + '</CharCode><Nominal>'
    end_str = '</Valute>'
    start_name_str = '<Name>'
    end_name_str = '</Name><Value>'
    end_nominal_str = '</Nominal>'
    start_value_str = '</Name><Value>'
    end_value_str = '</Value>'

    str_request = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if str_request.count(start_str) > 0:
        # Вырезаем из общего вывода информацию относящуюся к необходимой валюте.
        indx_str = str_request.index(start_str)
        str_request = str_request[indx_str+len(start_str):]
        indx_str = str_request.index(end_str)
        str_request = str_request[:indx_str]
        # Вырезаем номинал валюты (курс некоторых валют указан не за единицу, а например за 100 единиц).
        indx_str = str_request.index(end_nominal_str)
        nominal_currency = int(str_request[:indx_str])
        str_request = str_request[indx_str + len(end_nominal_str):]
        # Вырезаем название валюты на русском языке
        indx_str = str_request.index(start_name_str)
        str_request = str_request[indx_str+len(start_name_str):]
        indx_str = str_request.index(end_name_str)
        name_currency = str_request[:indx_str]
        # Вырезаем значение курса
        indx_str = str_request.index(start_value_str)
        str_request = str_request[indx_str + len(start_value_str):]
        indx_str = str_request.index(end_value_str)
        # курс в float
        val_currency_f = str_request[:indx_str]
        indx_str = val_currency_f.index(',')
        val_currency_f = float(val_currency_f[:indx_str] + '.' + val_currency_f[(indx_str + 1):])
        # собираем результаты в общую строку (float)
        print('Передаём значение курса через переменную float:')
        print(f'{nominal_currency} {name_currency}({currency_code.upper()}) = {val_currency_f:.2f} российских рублей.')

        # курс в Decimal
        getcontext().prec = 4
        val_currency_f = Decimal(str(val_currency_f))
        # собираем результаты в общую строку (Decimal)
        print('Передаём значение курса через переменную Decimal:')
        print(f'{nominal_currency} {name_currency}({currency_code.upper()}) = {1 * val_currency_f} российских рублей.')
        print('')

    else:
        print('None')

    #str_request.text


currency_rates('Eur')
currency_rates('usd')
currency_rates('CHF')
currency_rates('kzt')