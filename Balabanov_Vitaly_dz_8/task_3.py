# Задание 3
# Написать декоратор для логирования типов позиционных аргументов функции, например:
#
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
#
# $ a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#
# $ a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        result = func(*arg, **kwargs)
        for index, num in enumerate(arg):
            print(f'{calc_cube.__name__} ({arg[index]}: {type(arg[index])})')

        return result

    return  wrapper



@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)

# With several ellements
# def calc_cube(*x):
#    return sum(x) ** 3
#
# a = calc_cube(5,21,3)