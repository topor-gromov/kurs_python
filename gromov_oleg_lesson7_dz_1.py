"""
 Создаём словарь, в котором значение key это имя папки "первого уровня", а value: список с
именами подпапок. Разрешенно делать вложенные папки в подпапках, а также создавать более одной папки "первого уровня".
Пример: словарь вида
{'my_project': ['settings', {'mainapp': ['settings', 'temp']}, 'adminapp', 'authapp'], 'test': ['temp']}
корректно создаст две папки первого уровня my_project и test. В папке my_project создаст подпапки settings,
mainapp, adminapp, authapp, в подпапке mainapp создаст подпапки settings и temp. В папке test создаст подпапку temp.

"""
list_dir = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
start_path = 'd://'

import os
import sys


def create_dir(base_dir, list_dirt_def):
    try:
        if type(list_dirt_def) is dict:
            flag_add_dir = False
            for key_dir, value_dir in list_dirt_def.items():
                os.mkdir(os.path.join(base_dir, key_dir))
                if type(value_dir) is str:
                    if not flag_add_dir:
                        base_dir = base_dir + key_dir + '//'
                        flag_add_dir = True
                else:
                    base_dir = base_dir + key_dir + '//'
                    create_dir(base_dir, value_dir)
        elif type(list_dirt_def) is list:
            for elem in list_dirt_def:
                if type(elem) is str:
                    os.mkdir(os.path.join(base_dir, elem))
                elif type(elem) is dict:
                    create_dir(base_dir, elem)
    except FileExistsError:
        print('Папка уже существует!')
        sys.exit()


for key_path_dir, path_dir in list_dir.items():
    if path_dir != '':
        create_dir(start_path, {key_path_dir: path_dir})
    else:
        create_dir(start_path, [key_path_dir])

print('Стартер создан!')
