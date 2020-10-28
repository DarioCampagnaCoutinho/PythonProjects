import json
import sys

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
    resposta = requisicao(URL_ALL)
    if resposta:
        paises = parsing(resposta)
        if paises:
            return len(paises)


def mostrar_populacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print('{}: {}'.format(pais['name'], pais['population']))
    else:
        print('País não encontrado!')


def mostrar_moedas(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print('Moedas do pais : {}'.format(pais['name']))
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
    else:
        print('País não encontrado!')


def lista_de_paises(paises):
    for pais in paises:
        print(pais['name'])


def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("É preciso passar o nome do país")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("## Bem vindo ao sistema de países ##")
        print("Uso: python paises.py <ação> <nome do país>")
        print("Ações disponíveis: contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            numero_de_paises = contagem_de_paises()
            print("Existem {} países no mundo todo".format(numero_de_paises))
        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print("Argumento inválido")