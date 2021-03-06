# Задание 3 Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#
# Например:
#
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Подумайте:
#
# полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?
# ВНИМАНИЕ! Используйте стартовый код для своей реализации


def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        if name[0] in dict_out:
            dict_out[name[0]].append(name)
        else:
            dict_out[name[0]] = [name]
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
