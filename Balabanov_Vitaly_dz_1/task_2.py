# def sum_list_1(dataset: list) -> int:
#     """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
#     # место для написания кода
#     return 1  # Верните значение полученной суммы
#
#
# def sum_list_2(dataset: list) -> int:
#     """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
#         сумма цифр которых делится нацело на 7"""
#     # место для написания кода
#     return 1  # Верните значение полученной суммы


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""

    sum_digits = 0
    whole_number = 0

    for whole_number in dataset:

        for separate_digit in str(whole_number):
            sum_digits += int(separate_digit)

        if sum_digits % 7 == 0:
            whole_number += whole_number
    return whole_number  # Верните значение полученной суммы

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""

    sum_digits = 0
    whole_number = 0

    for whole_number in [x + 17 for x in dataset]:

        for separate_digit in str(whole_number):
            sum_digits += int(separate_digit)

        if sum_digits % 7 == 0:
            whole_number += whole_number

    return whole_number  # Верните значение полученной суммы



my_list = [number ** 3 for number in range(1000) if number % 2]  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)


