import sys
temp_list = []
flag_elem = False
if len(sys.argv) == 3: # два аргумента
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        indx_line = 1
        for line_file in f:
            if indx_line != int(sys.argv[1]):
                temp_list.append(line_file.strip('\n'))
            else:
                flag_elem = True
                temp_list.append(sys.argv[2])
            indx_line = indx_line + 1
    if flag_elem:
        with open('bakery.csv', 'w', encoding='utf-8') as f:
            for elem in temp_list:
                f.writelines(elem + '\n')
    else:
        print('Введённый Вами номер строки не существует, значение будет добавлено в конец файла!')
        with open('bakery.csv', 'a', encoding='utf-8') as f:
            f.writelines(sys.argv[2])

else: # без аргументов или НЕ 2 аргумента.
    print('Неккоректное количество параметров!')
