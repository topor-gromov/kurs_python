import sys

if len(sys.argv) == 1: # без аргументов
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line_file in f:
            print(line_file.strip('\n'))
elif len(sys.argv) == 2: # один аргумент
    indx_line = 1
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line_file in f:
            if indx_line >= int(sys.argv[1]):
                print(line_file.strip('\n'))
            indx_line = indx_line + 1
elif len(sys.argv) == 3: # два аргумента
    indx_line = 1
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line_file in f:
            if indx_line >= int(sys.argv[1]) and indx_line <= int(sys.argv[2]):
                print(line_file.strip('\n'))
            indx_line = indx_line + 1
