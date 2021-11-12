# постоянный словарь
number_dict = {'zero': 'нуль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(number, flag_english):
    """
    Функция печатает в консоль перевод введённого пользователем числа.
    :param number: Введённое пользователем значение.
    :param flag_english: Переменная указывающая на  каком языке пользователь ввёл текст (True - англ. False - русский)
    :return: None
    """
    if flag_english:
        index_number = number_dict.get(number)
        if index_number is not None:
            print(number_dict[number])
        else:
            print(index_number)
    else:
        find_elem = False
        for key, val in number_dict.items():
            if val == number:
                print(key)
                find_elem = True
                break
        if not find_elem:
            print('None')


# формируем два списка с английскими и русскими прописными буквами для проверки корректности ввода
letter_english = []
letter_russian = []

for code_letter in range(ord('a'), ord('z') + 1):
    letter_english.append(chr(code_letter))

for code_letter in range(ord('а'), ord('я') + 1):
    letter_russian.append(chr(code_letter))

number_user = input('Введите текстом число от 0 до 10: ').lower()

word_english = False
word_russian = False

# проверка на каком языке введены данные

for letter in number_user:
    if letter_english.count(letter) > 0:
        word_english = True
    if letter_russian.count(letter) > 0:
        word_russian = True

if word_english and not word_russian:
    num_translate(number_user, True)
elif not word_english and word_russian:
    num_translate(number_user, False)
else:
    print('None')
