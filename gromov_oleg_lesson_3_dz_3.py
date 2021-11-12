def thesaurus(*args):
    key_list_def = []
    dict_result = {}
    for names in args:
        if key_list_def.count(names[:1]) == 0:
            key_list_def.append(names[:1])

    for key_def in key_list_def:
        dict_result[key_def] = list(filter(lambda name: name[:1] == key_def, args))

    return dict_result

dict_names = thesaurus('Иван', 'Роман', 'Егор', 'Петр', 'Диана', 'Денис', 'Полина', 'Станислав', 'Никита', 'Елена')

print('Неотсортированный словарь:')
print('{')
for key, val in dict_names.items():
    print(f'{key:>6}: {val}')
print('}')

# сортировка словаря. Если нужно.
print('Отсортированный словарь:')
print('{')
key_list = []
for key in dict_names.keys():
    key_list.append(key)  # создаём список ключей

for key in sorted(key_list):
    print(f'{key:>6}: {dict_names[key]}')  # выводим элементы по отсортированным в списке ключам
print('}')
