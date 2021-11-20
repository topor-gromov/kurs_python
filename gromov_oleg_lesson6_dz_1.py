list_result = []
with open('nginx_logs.txt','r', encoding='utf-8') as f:

    for string_file in f:
        temp_list = f.readline().split()
        temp_tuple=(temp_list[0], temp_list[5][1:],temp_list[6])
        list_result.append(temp_tuple)

# для более читаемого вывода.
print('[')
for s in list_result:
    print(s)
print(']')