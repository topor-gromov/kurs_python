list_result = []
list_top = []
temp_list = []
list_user = []
with open('nginx_logs.txt','r', encoding='utf-8') as f:
    for string_file in f:
        list_result.append(f.readline().split()[0])
set_ip_list = set(list_result)

list_top = [str(list_result.count(num)) + '-' + str(num) for num in set_ip_list]

for elem in list_top:
    temp_list.append(int(elem[0:elem.index('-')]))

top_count = int(input('Введите количество пользователей, для вывода статистики: '))
if top_count > 0:
    for elem in sorted(temp_list, reverse=True)[:top_count]:
        list_user = [(num[num.index('-') + 1:]) for num in list_top if int(num[0:num.index('-')]) == elem]
        print(f'Пользователь/пользователи с IP-адресом/адресами: {list_user} отправили {elem} запросов.')
else:
    print('Вы ввели некорректное число!')