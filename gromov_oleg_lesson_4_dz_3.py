from requests import get
from datetime import *

def currency_rates(currency_code):
    # приводим введённый результат к верхнему регистру и формируем строку запроса.
    start_str = '<CharCode>' + str(currency_code).upper() + '</CharCode><Nominal>'
    end_str = '</Valute>'
    start_name_str = '<Name>'
    end_name_str = '</Name><Value>'
    end_nominal_str = '</Nominal>'
    start_value_str = '</Name><Value>'
    end_value_str = '</Value>'
    start_date_str = '<ValCurs Date="'
    end_date_str = '" name="Foreign Currency Market">'
    str_request = get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if str_request.count(start_str) > 0:
        # Формируем объект Date
        indx_str = str_request.index(start_date_str)
        date_string = str_request[indx_str + len(start_date_str):]
        indx_str = date_string.index(end_date_str)
        date_string = date_string[:indx_str]
        date_request = datetime.strptime(date_string, '%d.%m.%Y').date()
        date_request = date_request.strftime('%d.%m.%Y')
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
        print(f'Обменный курс {currency_code.upper()} к российскому рублю на {date_request}:')
        print(f'{nominal_currency} {name_currency}({currency_code.upper()}) = {val_currency_f:.2f} российских рублей.')
        print('')

    else:
        print('None')

currency_rates('Eur')
currency_rates('usd')
currency_rates('CHF')
currency_rates('kzt')