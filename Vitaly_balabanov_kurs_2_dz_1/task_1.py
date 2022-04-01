"""""
1. Посмотреть документацию к API GitHub, разобраться 
как вывести список наименований репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""""

import requests
import json
from pprint import pprint


params = {"username": "VitalyBalabanov"}

url = 'https://api.github.com/user/repos'

username = 'VitalyBalabanov'

token = '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'

response = requests.get(url, auth=(username, token), params=params)

j_date = response.json()


pprint(j_date)

with open('data.json', 'w') as f:
    for rep in j_date:
        json.dump(rep['name'], f, indent=4)

