def thesaurus_adv(*args):
    dict_temp = {}
    dict_result = {}
    l_name_list = []

    for names in args:  # создаём список с первыми буквами фамилий
        l_nam_indx = names.index(' ')
        l_nam_val = names[(l_nam_indx + 1):(l_nam_indx + 2)]
        if l_name_list.count(l_nam_val) == 0:
            l_name_list.append(l_nam_val)

    for key_def in l_name_list:  # создаём словарь. key = первая буква фамилии, value = список.
        dict_temp[key_def] = list(filter(lambda name: name[name.index(' ') + 1: name.index(' ') + 2] == key_def, args))

    for key_def, val_def in dict_temp.items():  # цикл по элементам словаря
        key_list_def = []
        val_dict = {}
        for names in val_def:  # создаём список с первыми буквами имён.
            if key_list_def.count(names[:1]) == 0:
                key_list_def.append(names[:1])
        for letter in key_list_def:  # формируем новый словарь с key = первой букве имени.
            val_dict[letter] = list(filter(lambda name: name[:1] == letter, val_def))
        dict_result[key_def] = val_dict

    return dict_result


# Функция для сортировки основного словаря и вложенных  в него словарей
def print_sort_dict(sorted_dict):
    for val in sorted(sorted_dict):
        if type(sorted_dict[val]) is not list:
            print(f'"{val}": ', '{')
            if len(sorted_dict[val]) == 1:
                for key_dict, val_dict in sorted_dict[val].items():
                    print(f'   "{key_dict}": {val_dict}')
            elif len(sorted_dict[val]) > 1:
                print_sort_dict(sorted_dict[val])
            print('}')
            print('')
        else:
            print(f'     "{val}": {sorted_dict[val]}')
            print('')

dict_names = thesaurus_adv('Иван Иванов', 'Роман Сергеев', 'Егор Смелов', 'Роберт Сидоров', 'Диана Арбенина')

print('Неотсортированный словарь:')
print('{')
for key, val in dict_names.items():
    print(f'"{key}": ', '{')
    for key_list, val_list in val.items():
        print(f'   "{key_list}": {val_list}')
    print('}')
    print('')

# сортировка словаря. Если нужно.

print('Отсортированный словарь:')
print('{')
print_sort_dict(dict_names)
