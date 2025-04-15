'''Desafio: Criar uma API que retorna o preço do dólar em tempo real
Objetivo: Criar uma API que retorna o valor do dólar comercial atual (em reais),
obtido de algum site confiável via scraping.'''
'''site padrão API BCB'''
'''https ://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/[codigo_recurso]?$format=json&[Outros Parâmetros]'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver # renderiza JavaScript
from datetime import datetime


def baixar(url_site):
    resposta = requests.get(url_site)
    if resposta.status_code == 200:
        print(resposta)
        print('=' * 50)
        print(resposta.headers['Content-Type'])
        print('=' * 50)
        print(resposta.text)
        print('='*50)
        print(resposta.content)
        print('=' * 50)
        print(resposta.url)
    else:
        print(f'erro: {resposta.status_code}')


def baixar2(url_site):
    driver = webdriver.Chrome() # instancia, simula um navegador de verdade e espera a página "terminar de carregar"
    driver.get(url_site) # não retorna enquanto a página não esteja totalmente carregada

    html = driver.page_source # obtem a fonte da página atual
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    #print(html)
    achados = soup.find('input', class_="form-control np-form-control np-form-control--size-auto np-input np-input--shape-rectangle", id='target-input')
    print(achados['value'])


def baixar3(url_site):
    resposta = requests.get(url_site)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    achados = soup.find('input', class_="form-control np-form-control np-form-control--size-auto np-input np-input--shape-rectangle", id='target-input')
    return achados['value']


site = 'https://www.bcb.gov.br/estabilidadefinanceira/fechamentodolar'
site2 = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moeda?$format=json'
site3 = "https://wise.com/br/currency-converter/dolar-hoje"
valor_dolar = baixar3(site3)

hoje = datetime.today().date()

print('=' * 20, 'COTAÇÃO DOLAR', '=' * 20) # 40 + 13 = 53
print(f'data: {hoje}\n')
print(f'\033[1m             1   USD     =     {valor_dolar}   BRL\033[0m')






