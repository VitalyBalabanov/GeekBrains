# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены
# в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

import os
import shutil


trg_path = '/Users/vitalybalabanov/PycharmProjects/Template'
walk_path = '/Users/vitalybalabanov/PycharmProjects/my_project'

if os.path.exists(trg_path):
    shutil.rmtree(trg_path)

for roots, dirs, files in os.walk(walk_path):
    for dir in dirs:
        if roots.endswith('/templates'):
            shutil.copytree(roots, os.path.join(trg_path, dir))

