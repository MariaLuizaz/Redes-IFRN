#questão 2 da lista 4 

import requests
strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
dictCartola = requests.get(strURL).json()

import sys
import datetime
from datetime import date 

ano = int(input('Informe o ano desejado:'))
ano_atual = date.today().year

if ano > ano_atual:
    print('O ano informado não pode ser superior ao ano atual!!')
    sys.exit()

import json 

try:
    if ano == ano_atual:
        strURL = 'https://api.cartolafc.globo.com/atletas/mercado'
        dictCartola = requests.get(strURL).json()
    else:
        nome_arquivo = f'cartola_fc_{ano}.json'
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            dictCartola = json.load(file)
except requests.exceptions.RequestException as e:
    print('Erro ao fazer a requisição:', e)
    exit()
except FileNotFoundError:
    print(f'O arquivo {nome_arquivo} não foi encontrado.')
    exit()
except json.JSONDecodeError:
    print(f'Erro ao decodificar o arquivo {nome_arquivo}.')
    exit()
except UnicodeDecodeError:
    print(f'Erro ao decodificar o arquivo {nome_arquivo}.')
    exit()

escalacao_ok = {
    1: '3-4-3',
    2: '3-5-2',
    3: '4-3-3',
    4: '4-4-2',
    5: '4-5-1',
    6: '5-3-2',
    7: '5-4-1'
}

import tabulate
from tabulate import tabulate

print('Escolha uma das escalações:')
tabela_esc = [[num, escalacao] for num, escalacao in escalacao_ok.items()]
print(tabulate(tabela_esc, headers=['NÚMERO', 'ESCALAÇÃO'], tablefmt='fancy_grid'))

try:
    escalacao_input = int(input('Informe o número da escalação que você deseja: '))
except ValueError:
    print('ERRO! Insira um número inteiro.')
    exit()

if escalacao_input < 1 or escalacao_input > 7:
    print('ERRO! Escolha a escalação de acordo com a tabela!!!')
    sys.exit()

esquemas_taticos = {
    '3-4-3': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 4, 'atacante': 3, 'tecnico': 1},
    '3-5-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 0, 'meia': 5, 'atacante': 2, 'tecnico': 1},
    '4-3-3': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 3, 'atacante': 3, 'tecnico': 1},
    '4-4-2': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 4, 'atacante': 2, 'tecnico': 1},
    '4-5-1': {'goleiro': 1, 'zagueiro': 2, 'lateral': 2, 'meia': 5, 'atacante': 1, 'tecnico': 1},
    '5-3-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 3, 'atacante': 2, 'tecnico': 1},
    '5-4-1': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 4, 'atacante': 1, 'tecnico': 1},
}

esquema_selecionado = escalacao_ok[escalacao_input]
quantidade_posicoes = esquemas_taticos[esquema_selecionado]

selecionados = {}

for posicao, quantidade in quantidade_posicoes.items():
    posicao_id = {
        'goleiro': 1,
        'zagueiro': 3,
        'lateral': 2,
        'meia': 4,
        'atacante': 5,
        'tecnico': 6
    }[posicao]
    
    jogadores = [atleta for atleta in dictCartola['atletas'] if atleta['posicao_id'] == posicao_id]
    
    for atleta in jogadores:
        atleta['pontuacao_total'] = round(atleta.get('media_num', 0) * atleta.get('jogos_num', 0), 2)
    
    jogadores = sorted(jogadores, key=lambda x: x.get('pontuacao_total', 0), reverse=True)[:quantidade]
    
    selecionados[posicao] = jogadores

cartola_selecao = {}

for posicao, atletas in selecionados.items():
    for atleta in atletas:
        id_atleta = atleta['atleta_id']
        foto_url = atleta.get('foto', '')
        foto_url = foto_url.replace('_FORMATO_', '_220x220_').replace('_FORMATO', '_220x220')

        clube_id = str(atleta['clube_id'])
        clube_nome = dictCartola['clubes'].get(clube_id, {}).get('nome', 'Clube Desconhecido')
        escudo_url = dictCartola['clubes'].get(clube_id, {}).get('escudos', {}).get('60x60', '')

        cartola_selecao[id_atleta] = {
            'id': id_atleta,
            'nome': atleta.get('nome', 'Desconhecido'),
            'apelido': atleta.get('apelido', 'sem Apelido'),
            'url_foto': foto_url,
            'clube': clube_nome,
            'escudo': escudo_url,
            'id_posicao': atleta['posicao_id'],
            'nome_posicao': posicao,
            'pontuacao': atleta.get('pontuacao_total', 0)
        }

try:
    with open(f'cartola_selecao_{esquema_selecionado}_{ano}.json', 'w', encoding='utf-8') as outfile:
        json.dump(cartola_selecao, outfile, indent=4, ensure_ascii=False, )
except IOError:
    print('Erro ao salvar o arquivo JSON.')
    exit()

print('\nSeleção do Cartola FC:')
tabela_selecao = []
for posicao in ['goleiro', 'zagueiro', 'lateral', 'meia', 'atacante', 'técnico']:
    if posicao in selecionados:
        for atleta in selecionados[posicao]:
            clube_id = str(atleta['clube_id'])
            clube_nome = dictCartola['clubes'].get(clube_id, {}).get('nome', 'Clube Desconhecido')
            tabela_selecao.append([
                atleta['nome'],
                atleta['apelido'],
                clube_nome,
                posicao.capitalize(),
                f'{atleta.get('pontuacao_total', 0):.2f}'
            ])
print(tabulate(tabela_selecao, headers=['Nome', 'Apelido', 'Clube', 'Posição', 'Pontuação'], tablefmt='fancy_grid'))
