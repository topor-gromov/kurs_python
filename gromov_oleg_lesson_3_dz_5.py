import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count_jokes, flag_repeater):
    """
    Функция генерирует предложения из слов содержащихся в трёх списках (по одному слову из каждого списка).
    :param count_jokes: параметр указывающий необходимое количество сгенерированных предложений
            flag_repeater: Логическая переменная указывающая возможность повтора слов в сгенерированных предложениях.
            True - повтор разрешен, False - повтор запрещён.
    :return: возвращает список сгенерированных предложений
    """
    def_list_jokes = []
    rand_nouns = nouns.copy()
    rand_adverbs = adverbs.copy()
    rand_adjectives = adjectives.copy()
    for indx in range(1, count_jokes + 1):
        nouns_word = random.choice(rand_nouns)
        rand_nouns.pop(rand_nouns.index(nouns_word))
        adverbs_word = random.choice(rand_adverbs)
        rand_adverbs.pop(rand_adverbs.index(adverbs_word))
        adjectives_word = random.choice(rand_adjectives)
        rand_adjectives.pop(rand_adjectives.index(adjectives_word))
        if flag_repeater:
            def_list_jokes.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
        else:
            def_list_jokes.append(nouns_word + ' ' + adverbs_word + ' ' + adjectives_word)
    return def_list_jokes


def get_jokes_adv(**kwargs):
    """
    Функция генерирует предложения из слов содержащихся в трёх списках (по одному слову из каждого списка).
    :param **kwargs принимает именованные параметры:
            count_jokes: параметр указывающий необходимое количество сгенерированных предложений
            flag_repeater: Логическая переменная указывающая возможность повтора слов в сгенерированных предложениях.
            True - повтор разрешен, False - повтор запрещён.
    :return: возвращает список сгенерированных предложений
    """
    count_jokes = int(kwargs['count_jokes'])
    flag_repeater = bool(kwargs['flag_repeater'])

    def_list_jokes = []
    rand_nouns = nouns.copy()
    rand_adverbs = adverbs.copy()
    rand_adjectives = adjectives.copy()
    for indx in range(1, count_jokes + 1):
        nouns_word = random.choice(rand_nouns)
        rand_nouns.pop(rand_nouns.index(nouns_word))
        adverbs_word = random.choice(rand_adverbs)
        rand_adverbs.pop(rand_adverbs.index(adverbs_word))
        adjectives_word = random.choice(rand_adjectives)
        rand_adjectives.pop(rand_adjectives.index(adjectives_word))
        if flag_repeater:
            def_list_jokes.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
        else:
            def_list_jokes.append(nouns_word + ' ' + adverbs_word + ' ' + adjectives_word)
    return def_list_jokes


list_jokes = get_jokes(5, False) 
for jokes in list_jokes:
    print(jokes)

print('')
print('Функция с именованными аргументами:')
list_jokes = get_jokes_adv(flag_repeater = False, count_jokes = 3)
for jokes in list_jokes:
    print(jokes)
