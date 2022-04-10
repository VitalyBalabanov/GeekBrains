# Задание 3
# Есть два списка:
#
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
#
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект.
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Vitaly', 'Sergey', 'Viktor']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen( tutors: list, klasses: list):
    diff_value = len(tutors) - len(klasses)
    if diff_value > 0:
        for i in range(diff_value):
            klasses.append(None)
    for name_class_number in zip(tutors, klasses):
        yield (name_class_number)


generator = check_gen(tutors, klasses)

print(type(generator))

for name_class_number in generator:
    print(next(generator))


