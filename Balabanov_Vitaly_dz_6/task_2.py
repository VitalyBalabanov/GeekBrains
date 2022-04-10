# Есть два файла users.csv и hobby.csv: в первом хранятся ФИО пользователей сайта,
# а во втором — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби (список строковых переменных). Сохранить словарь в файл task_6_3_result.json. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом 1.
#
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    user_inform = {}
    user_file = open(path_users_file, 'r', encoding='utf-8')
    hobby_file = open(path_hobby_file, 'r', encoding='utf-8')
    while True:
        name_line = user_file.readline()
        if not name_line:
            break
        hobby_line = hobby_file.readline().strip()
        user_key = name_line.strip().replace(",", " ")
        if len(user_key) == 0:
            print(1)
            break
        elif len(hobby_line) == 0:
            hobby_line = None
            user_inform[user_key] = hobby_line
        else:
            user_inform[user_key] = hobby_line.strip()
    user_file.close()
    hobby_file.close()
    return user_inform


dict_out = prepare_dataset('users', 'hobby')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)