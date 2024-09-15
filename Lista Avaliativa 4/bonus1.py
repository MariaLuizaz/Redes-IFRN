#bonus da questão 1 

import requests
import datetime
import sys
import json
import os 

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURL += '/Moedas?$top=100&$format=json'
dictMoedas = requests.get(strURL).json()
strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&'
strURL += f'@dataFinalCotacao=%2712-31-2023%27&$format=json'
dictCotacoes = requests.get(strURL).json()

from datetime import date
ano = int(input('Informe o ano desejado:'))
ano_atual = date.today().year

if ano > ano_atual:
     print(f'ERRO! O ano informado não pode ser superior ao ano atual!!')
     sys.exit()

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json'

try:
    response = requests.get(strURL)
    response.raise_for_status()
    dictMoedas = response.json()
except requests.exceptions.RequestException as e:
    print(f'Erro ao acessar a API: {e}')
    exit()
except ValueError as e:
    print(f'Erro ao interpretar a resposta da API como JSON: {e}')
    exit()

try:
    response = requests.get(strURL)
    dictMoedas = response.json()
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except ValueError as e:
    print(f"Erro ao decodificar JSON: {e}")


moedas_ok = [(moeda['simbolo'], moeda['nomeFormatado']) for moeda in dictMoedas.get('value', [])]
if not moedas_ok:
    print('Nenhuma moeda foi encontrada na API.')
    exit()
from tabulate import tabulate
tabela_m = tabulate(moedas_ok, headers=['Sigla', 'Nome da Moeda'], tablefmt='fancy_grid')

print('\nMoedas Disponíveis:')
print(tabela_m)

moeda_input = str(input('Informe a moeda desejada de acordo com a tabela exibida:')).upper()

if moeda_input not in tabela_m:
    print('ERRO! Esta moeda não é válida! Escolha de acordo com a tabela!!')
    sys.exit()

strURL = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURL += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURL += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURL += f'@moeda=%27{moeda_input}%27&@dataInicial=%2701-01-{ano}%27&'
strURL += f'@dataFinalCotacao=%2712-31-{ano}%27&$format=json'
try:
    response = requests.get(strURL)
    response.raise_for_status()
    dictCotacoes = response.json()
except requests.exceptions.RequestException as e:
    print(f'Erro ao acessar a API: {e}')
    print('Tente novamente.')
    exit()
except ValueError as e:
    print(f'Erro ao interpretar a resposta da API como JSON: {e}')
    sys.exit()

if not dictCotacoes.get('value'):
    print('Não há dados disponíveis para a moeda e o ano desejados.')
    sys.exit()

medias = {}
for cotacao in dictCotacoes['value']:
    try:
        data = cotacao['dataHoraCotacao'].split('T')[0]
        mes = data[5:7]
        if mes not in medias:
            medias[mes] = {'mediaCompra': [], 'mediaVenda': []}
        if cotacao['cotacaoCompra'] is not None and cotacao['cotacaoVenda'] is not None:
            medias[mes]['mediaCompra'].append(float(cotacao['cotacaoCompra']))
            medias[mes]['mediaVenda'].append(float(cotacao['cotacaoVenda']))
    except (KeyError, ValueError) as e:
        print(f'Erro ao processar dados: {e}')
        continue

medias_ok = {}
for mes in medias:
    if medias[mes]['mediaCompra'] and medias[mes]['mediaVenda']:
        mediaC = sum(medias[mes]['mediaCompra']) / len(medias[mes]['mediaCompra'])
        mediaV = sum(medias[mes]['mediaVenda']) / len(medias[mes]['mediaVenda'])
        medias_ok[mes] = {
            'mediaCompra': round(mediaC, 5),
            'mediaVenda': round(mediaV, 5)}
        
nome_arquivo_json = f'medias_cotacoes_{moeda_input}_{ano}.json'
nome_arquivo_csv = f'medias_cotacoes_{moeda_input}_{ano}.csv'

if os.path.exists(nome_arquivo_json):
    print(f'O arquivo {nome_arquivo_json} já existe e será sobrescrito.')
if os.path.exists(nome_arquivo_csv):
    print(f'O arquivo {nome_arquivo_csv} já existe e será sobrescrito.')

try:
    with open(nome_arquivo_json, 'w') as json_file:
        json.dump(medias_ok, json_file, indent=4)
except IOError as e:
    print(f'Erro ao salvar o arquivo JSON: {e}')
    sys.exit()

try:
    with open(nome_arquivo_csv, 'w') as csv_file:
        csv_file.write('moeda;mes;mediaCompra;mediaVenda\n')
        for mes in medias_ok:
            csv_file.write(f'{moeda_input};{mes};{medias_ok[mes]['mediaCompra']};{medias_ok[mes]['mediaVenda']}\n')
except IOError as e:
    print(f'Erro ao salvar o arquivo CSV: {e}')
    sys.exit()

print('SUCESSO!!!')

#parte bônus

import matplotlib
import matplotlib.pyplot as graf

meses = sorted(medias_ok.keys())
mediaCompra = [medias_ok[mes]['mediaCompra'] for mes in meses]
mediaVenda = [medias_ok[mes]['mediaVenda'] for mes in meses]

graf.figure(figsize=(8, 5))
graf.plot(meses, mediaCompra, label='Média Compra', color='blue', marker='o')
graf.plot(meses, mediaVenda, label='Média Venda', color='purple', marker='o')
graf.title(f'Média Cotações {moeda_input} – Ano {ano}')
graf.xlabel('Mês')
graf.ylabel('Valor')
graf.legend()
graf.grid(True)
graf.show()

print('SUCESSO!!!')