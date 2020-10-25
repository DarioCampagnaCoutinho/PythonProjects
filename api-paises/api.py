import requests


URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name/Brasil'

resp1 = requests.get(URL_ALL)
resp2 = requests.get(URL_NAME)

print(resp2.text)