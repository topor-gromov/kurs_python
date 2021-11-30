import os
import shutil

start_path = 'd://my_project//'
list_templates = ['index.html', 'base.html'] # Список файлов для поиска.
dest_path = 'templates//' # Имя папки в которую будем копировать найденные файлы.

for root, dirs, files in os.walk(start_path):

    for elem in files:
        if list_templates.count(str(elem)) > 0:
            try:
                os.mkdir(os.path.join(start_path, dest_path))
            except FileExistsError:
                pass

            try:
                os.mkdir(os.path.join(start_path + dest_path + os.path.basename(root) + '//'))
            except FileExistsError:
                pass

            try:
                if (root + '//' + elem) != (start_path + dest_path + os.path.basename(root) + '//' + elem):
                    shutil.copy2(root + '//' + elem, start_path + dest_path + os.path.basename(root) + '//' + elem)
            except Exception: # Ошибку о том что файл уже существует генерирует модуль shutil, не системная, как отловить конкретно её, не нашёл.
                pass

print('Копирование шаблонов завершено!')
