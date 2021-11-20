import os
import sys
dict_users = {}
users_file = os.path.abspath('users.csv')
hobby_file = os.path.abspath('hobby.csv')
result_file = os.path.abspath('result.csv')
indx_elem = 0
list_hobby = []
with open(users_file,'r', encoding='utf-8') as f:
    str_users = f.read().split()
    hobby_f = open(hobby_file, 'r', encoding='utf-8')
    str_hobbys = hobby_f.read().splitlines()
    for str_user in str_users:
        str_key = str_user.replace(',', ' ', 2)
        if indx_elem < len(str_hobbys):
            dict_users[str_key] = str_hobbys[indx_elem]
        else:
            dict_users[str_key] = 'None'
        indx_elem = indx_elem + 1
    hobby_f.close()

with open(result_file, 'w', encoding='utf-8') as f:
    print(dict_users, file=f)

# Из задания мне не понятно нужно ли, если список с хобби больше списка с ФИО, выходить сразу или вначале нужно
# внести данные в файл. Сделал по второму варианту. Первый вариант в задаче №4
if len(str_hobbys) > len(str_users):
    sys.exit(1)