from requests import get, utils
from datetime import date
response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(manys):
    content = response.split("<Valute ID=")
    d, m , y = map(int, content[0].split('"')[-4].split("."))
    for i in content:
        if manys.upper() in i:
            print(date(year=y, month=m, day=d), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))