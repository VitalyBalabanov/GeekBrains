# Задание 1
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#
# $ odd_to_15 = odd_nums(15)
# $ next(odd_to_15)
# 1
# $ next(odd_to_15)
# 3
# ...
# $ next(odd_to_15)
# 15
# $ next(odd_to_15)
# ...StopIteration...
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:


def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for number in range(1, n + 1, 2):
        yield number


n = 15
generator = odd_nums(n)
for number in generator:
     print(number)
