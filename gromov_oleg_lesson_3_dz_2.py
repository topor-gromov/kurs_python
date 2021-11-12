# постоянный словарь
number_dict = {'zero': 'нуль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate_adv(number,flag_english):
    """
    Функция возвращает тестовую переменную с переводом введённого пользователем слова
    :param number: Введённое пользователем значение.
    :param flag_english: Переменная указывающая на  каком языке пользователь ввёл текст (True - англ. False - русский)
    :return: Текстовая переменная с переводом слова.
    """
    result_word = None
    if flag_english:
        index_number = number_dict.get(number)
        if index_number is not None:
            result_word = number_dict[number]
        else:
            result_word = index_number

    else:
        find_elem = False
        for key, val in number_dict.items():
            if val == number:
                result_word = key
                find_elem = True
                break

    return result_word

# формируем два списка с английскими и русскими прописными буквами для проверки корректности ввода
letter_english = []
letter_russian = []


for code_letter in range(ord('a'),ord('z')+1):
    letter_english.append(chr(code_letter))

for code_letter in range(ord('а'),ord('я')+1):
    letter_russian.append(chr(code_letter))


number_user_source = input('Введите текстом число от 0 до 10: ')
number_user = number_user_source.lower()

word_english = False
word_russian = False


# проверка на каком языке введены данные

for letter in number_user:
    if letter_english.count(letter) > 0:
        word_english = True
    if letter_russian.count(letter) > 0:
        word_russian = True

if word_english and not word_russian:
    result_message = num_translate_adv(number_user,True)
elif not word_english and word_russian:
    result_message = num_translate_adv(number_user,False)
else:
    result_message = 'None'

# проверяем с какой буквы пользователь ввёл слово.
if number_user_source[:1].isupper():
    print(result_message.title())
else:
    print(result_message)