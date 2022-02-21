# Урок 6. Работа с файлами
# Задание 1
# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
#
#  Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:

from pprint import pprint

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line = line.split(" ")
    list_out = tuple(list((line[0], line[5].replace('"', ''), line[6])))
    pprint(list_out)


list_out = list()
with open('nginx_logs', 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line:
            break
        get_parse_attrs(line)

