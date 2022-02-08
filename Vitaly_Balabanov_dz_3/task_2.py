# Задание 2
# *(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
#
# Например:
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
            'Seven': 'семь', 'eight': 'восемь', 'nine': 'деветь', 'ten': 'десять'}


def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    if value[0].isupper():
        str_out = num_dict.get(value.lower()).capitalize()
    else:
        str_out = num_dict.get(value.lower())
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("eight"))


