# Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os
import re
import shutil

to_remove_dir_name = '/Users/vitalybalabanov/PycharmProjects/my_project'
if os.path.exists(to_remove_dir_name):
    shutil.rmtree(to_remove_dir_name)

config_file_path = '/Users/vitalybalabanov/PycharmProjects/GeekBrains/Balabanov_Vitaly_dz_7/config.yaml'

base_project_path = '/Users/vitalybalabanov/PycharmProjects/'

with open(config_file_path, 'r', encoding='utf-8') as fr:
    first_letter = 6
    last_first_letter = 6
    last_config_path = ''
    project_name = fr.readline()
    project_name = re.sub('[|\-\-\\t\\n\\r ]', '', project_name)
    project_path = os.path.join(base_project_path, project_name)
    os.mkdir(project_path)
    os.chdir(project_path)
    while True:
        config_path = ''
        is_file_flag = 0
        config_name = fr.readline()
        if not config_name:
            break
        first_letter = re.search(r'[A-Za-z0-9\_\_]', config_name).start()
        config_name = re.sub('[|\-\-\\t\\n\\r ]', '', config_name)
        if config_name.endswith('.py') or config_name.endswith('.html'):
            is_file_flag = 1
        if first_letter == last_first_letter:
            config_path = os.path.join(os.getcwd(), config_name)
            if is_file_flag:
                with open(config_path, 'w') as fw:
                    pass
            else:
                os.mkdir(config_path)
        elif first_letter > last_first_letter:
            config_path = os.path.join(last_config_path, config_name)
            if is_file_flag:
                with open(config_path, 'w') as fw:
                    config_path, _ = os.path.split(config_path)
            else:
                os.mkdir(config_path)
            os.chdir(config_path)
        else:
            for _ in range(((last_first_letter - first_letter) // 3)):
                os.chdir('..')
            config_path = os.path.join(os.getcwd(), config_name)
            if is_file_flag:
                with open(config_path, 'w') as fw:
                    pass
            else:
                os.mkdir(config_path)
        last_first_letter = first_letter
        last_config_path = config_path




