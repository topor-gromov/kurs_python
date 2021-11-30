import os

st_path = 'd://my_project//some_data//'
size_thr_start = -1 #для того чтобы входили файлы с нулевым размером.
size_thr_end = 10
f_dict = {f.name:os.stat(st_path + f.name).st_size for f in os.scandir(st_path) if os.path.isfile(st_path + f.name)}

count_files = len(f_dict)
f_list = []
result_dict = {}

while count_files > 0:
    f_list = [value for key, value in f_dict.items() if (int(value) > size_thr_start) and (int(value) <= size_thr_end)]
    result_dict[size_thr_end] = len(f_list)
    count_files = count_files - len(f_list)
    size_thr_start = size_thr_end
    size_thr_end = size_thr_end * 10


print('{')
for key, value in result_dict.items():
    print(f'Файлов размером до {key} байт: {value} шт.')
print('}')