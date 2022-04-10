# Задание 5
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать
# из этих элементов список с сохранением порядка их следования в исходном списке, например:
#
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:





def get_uniq_numbers(src: list):
    unq_numbers = set()
    all_numbers = set()
    for number in src:
        if number not in all_numbers:
            unq_numbers.add(number)
        else:
            unq_numbers.discard(number)
        all_numbers.add(number)
    unique_brands_ord = [number_ord for number_ord in src if number_ord in unq_numbers]
    return unique_brands_ord


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
