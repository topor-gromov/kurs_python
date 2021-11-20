import sys
dict_users = {}
users_file = sys.argv[1]
hobby_file = sys.argv[2]
result_file = sys.argv[3]
indx_elem = 0
str_users = []
str_hobbys = []
str_result = []
str_user_value = []
str_hobby_value = []

with open(users_file, 'r', encoding='utf-8') as f:
    for line_file in f:
        str_users.append(line_file.strip('\n'))

with open(hobby_file, 'r', encoding='utf-8') as f:
    for line_file in f:
        str_hobbys.append(line_file.strip('\n'))

# Из задания мне не понятно нужно ли, если список с хобби больше списка с ФИО, выходить сразу или вначале нужно
# внести данные в файл. Сделал по первому варианту. Второй вариант в задаче №3.
if len(str_hobbys) > len(str_users):
    print('Список "ФИО" меньше списка "Хобби".')
    sys.exit(1)

# Формирую список из словарей для каждого пользователя. Хобби храниться в виде списка (если более одного хобби, для одного человека).
for str_user in str_users:
    dict_users = {}
    str_hobby_value = []
    str_user_value = str_user.replace(',', ' ').split()
    dict_users['Фамилия'] = str_user_value[0]
    dict_users['Имя'] = str_user_value[1]
    dict_users['Отчество'] = str_user_value[2]
    if indx_elem < len(str_hobbys): #Проверка если список хобби не закончился.
        if str_hobbys[indx_elem].count(',') > 0:
            str_hobby_value = str_hobbys[indx_elem].replace(',', ' ').split()
            dict_users['Хобби'] = str_hobby_value
        else:
            str_hobby_value.append(str_hobbys[indx_elem])
            dict_users['Хобби'] = str_hobby_value
    else:  # Если список хобби закончился, вносим None.
        str_hobby_value.append('None')
        dict_users['Хобби'] = str_hobby_value
    indx_elem = indx_elem + 1
    str_result.append(dict_users)

with open(result_file, 'w', encoding='utf-8') as f:
    print(str_result, file=f)

