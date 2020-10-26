import json

import requests


URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer conexão : ', url)


def parsing(resposta):
    try:
        return json.loads(resposta)
    except:
        print('Erro ao fazer o parsing!')


def contagem_de_paises(paises):
    return len(paises)


def mostrar_populacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print('{}: {}'.format(pais['name'], pais['population']))
        else:
            print('Pais não encontrado!')


def lista_de_paises(paises):
    for pais in paises:
        print(pais['name'])


if __name__ == '__main__':
    mostrar_populacao('brazil')