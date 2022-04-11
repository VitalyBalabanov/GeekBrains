"""
Вариант 1
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы
получаем должность)
с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта
(также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
Наименование вакансии.
Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
Ссылку на саму вакансию.
Сайт, откуда собрана вакансия.
"""

import requests
import string
from pprint import pprint
from bs4 import BeautifulSoup as bs



position = 'Python'

url = 'https://samara.hh.ru/search/vacancy?area=78&fromSearchLine=true&text'

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' \
          '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}

page = 0

position_dict = {}

list_of_all_positions = []

next_page = True


while next_page:

    position_url = f'{url}={position}&page={page}&hhtmFrom=vacancy_search_list'

    response = requests.get(position_url, headers=header)

    dom = bs(response.text, 'html.parser')

    positions = dom.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})

    for position in positions:
        position_info_list_len = 0
        position_info = position.find_all('span')
        position_info_list = position_info[2].text.replace('\u202f', '').split(' ')
        if 'от' in position_info_list:
            position_info_list.remove('от')
        if '–' in position_info_list:
            position_info_list.remove('–')
        position_dict['position_name'] = position_info[1].text
        position_info_list_len = len(position_info_list)
        if position_info_list_len == 1 and position_info_list[0] != '':
            position_dict['min_salary'] = position_info_list[0]
        else:
            position_dict['min_salary'] = None
        if position_info_list_len == 2:
            position_dict['min_salary'] = position_info_list[0]
            position_dict['max_salary'] = position_info_list[1]
        else:
            position_dict['max_salary'] = None
        if position_info_list_len == 3:
            position_dict['min_salary'] = position_info_list[0]
            position_dict['max_salary'] = position_info_list[1]
            position_dict['currency'] = position_info_list[2]
        else:
            position_dict['currency'] = None
        print(position_dict)
    next_page = dom.find_all('a', {'class': 'bloko-button','data-qa':'pager-next'})
    page += 1






