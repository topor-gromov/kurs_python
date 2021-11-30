import os

st_path = 'd://my_project//some_data//'
siz_st = -1 #для того чтобы входили файлы с нулевым размером.
siz_end = 10

f_dic = {f.name:os.stat(st_path + f.name).st_size for f in os.scandir(st_path) if os.path.isfile(st_path + f.name)}

count_files = len(f_dic)
f_list = []
ext_list =[]
result_dict = {}

while count_files > 0:
    f_list = [val for key, val in f_dic.items() if (val > siz_st) and (val <= siz_end)]
    ext_set = [key[((str(key)).index('.') + 1):] for key, val in f_dic.items() if (val > siz_st) and (val <= siz_end)]
    ext_set = list(set(ext_set))
    result_dict[siz_end] = (len(f_list), ext_set)
    count_files = count_files - len(f_list)
    siz_st = siz_end
    siz_end = siz_end * 10

# Форматированный вывод данных.
print('{')
for key, value in result_dict.items():
    print(f'Файлов размером до {key} байт: {value[0]} шт. список расширений {value[1]}')
print('}')

# неформатированный вывод данных.
print('{')
for key, value in result_dict.items():
    print(key, value)
print('}')