import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    site_text = response.text
    currency_dict = {}
    for index_row, row in enumerate(site_text.split('ID=')):
        if index_row == 0:
            pass
        else:
            char_code = row[row.find('<CharCode>'):row.find('</CharCode>')].replace('<CharCode>', '').title()
            currency_dict.pop('', None)
            nominal = float(
                            row[row.find('<Nominal>'):row.find('</Nominal>')].replace('<Nominal>', '').replace(',', '.')
                            )
            currency_dict[char_code] = float(
                                              row[row.find('<Value>'):row.find('</Value><')].replace('<Value>', '').replace(',', '.')
                                            ) / nominal

    result_value = currency_dict.get(code.title())
    return result_value


if __name__ == '__main__':

    print(currency_rates("USD"))
    print(currency_rates("eur"))
    print(currency_rates("noname"))