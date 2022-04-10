# Задание 1
# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять
# имена папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках
# и файлах (добавлять детали)?

import os

project_path = '/Users/vitalybalabanov/PycharmProjects/'

project_name = 'my_project'

starter_path = os.path.join(project_path, project_name)

sub_folder_list =['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(starter_path):
    os.mkdir(starter_path)

for folder in sub_folder_list:
    sub_folder_path = os.path.join(starter_path, folder)
    if not os.path.exists(sub_folder_path):
        os.mkdir(sub_folder_path)