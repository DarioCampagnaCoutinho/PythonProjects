import json

import requests


URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name/Brasil'

resp1 = requests.get(URL_ALL)

paises = json.loads(resp1.text)

for pais in paises:
    print(pais['name'], pais['capital'], pais['currencies'])