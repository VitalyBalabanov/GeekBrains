# На вход будет выдаваться список, пример:
#
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
#
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# b) Сформировать из обработанного списка строку:
#
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
#
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:


def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    _index = [list_in.index(word) for word in list_in if (any(character.isdigit() for character in word))]
    for i, number in enumerate(_index):
        list_in.insert(number + i, '"')
    _index = [list_in.index(word) for word in list_in if (any(character.isdigit() for character in word))]

    for number in _index:
        list_in[number] = '{:02}'.format(int(list_in[number]))

    for i, number in enumerate(_index):
        list_in.insert(number + i + 1, '"')

    str_out = ' '.join(list_in)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
