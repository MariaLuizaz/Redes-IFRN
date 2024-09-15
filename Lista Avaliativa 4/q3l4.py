import random
import tabulate
from tabulate import tabulate
import time
import ast 

def GerarCartelas(c):
    if c < 1 or c > 10000:
        return False, '/ERRO! Só é possível gerar até 10.000 cartelas.'
    
    cartelas = {}
    for _ in range(c):
        while True:
            qtd_cartelas = f'CART_{random.randint(1,10000):06}'
            if qtd_cartelas not in cartelas:
                cartela = {
                    'B': random.sample(range(1, 16), 5),
                    'I': random.sample(range(16, 31), 5),
                    'N': random.sample(range(31, 46), 4) + [0],  
                    'G': random.sample(range(46, 61), 5),
                    'O': random.sample(range(61, 76), 5)
                }
                cartelas[qtd_cartelas] = cartela
                break
    return True, cartelas

def SalvarCartelas(cartelas):
    nomearq = 'cartelas.txt'
    with open(nomearq, 'w') as file:
        for numero_cartela, cartela in cartelas.items():
            cartela_str = {letra: ','.join(map(str, nums)) for letra, nums in cartela.items()}
            file.write(f'{numero_cartela}: {cartela_str}\n')
    print(f'\nCartelas salvas com sucesso em {nomearq}!')
    time.sleep(2)

def LerCartelas():
    nomearq = 'cartelas.txt'
    cartelas = {}
    with open(nomearq, 'r') as file:
        for linha in file:
            p = linha.strip().split(': ', 1)
            numero_cartela = p[0]
            cartela_dados_str = p[1]
            cartela_dados = ast.literal_eval(cartela_dados_str) 
            cartela = {
                'B': list(map(int, cartela_dados['B'].split(','))),
                'I': list(map(int, cartela_dados['I'].split(','))),
                'N': list(map(int, cartela_dados['N'].split(','))),
                'G': list(map(int, cartela_dados['G'].split(','))),
                'O': list(map(int, cartela_dados['O'].split(',')))
            }
            cartelas[numero_cartela] = cartela
    return cartelas

def ImprimirCartelas(cartelas, numero_cartela):
    cartela = cartelas.get(numero_cartela)
    if not cartela:
        print(f'Número da cartela não encontrado: {numero_cartela}')
        return
    tabela = [
        ['B', 'I', 'N', 'G', 'O'],
        [cartela['B'][0], cartela['I'][0], cartela['N'][0], cartela['G'][0], cartela['O'][0]],
        [cartela['B'][1], cartela['I'][1], cartela['N'][1], cartela['G'][1], cartela['O'][1]],
        [cartela['B'][2], cartela['I'][2], cartela['N'][2], cartela['G'][2], cartela['O'][2]],
        [cartela['B'][3], cartela['I'][3], cartela['N'][3], cartela['G'][3], cartela['O'][3]],
        [cartela['B'][4], cartela['I'][4], cartela['N'][4], cartela['G'][4], cartela['O'][4]]
    ]
    print(f'\nCartela : {numero_cartela}')
    resultado = tabulate(tabela, headers='firstrow', tablefmt='fancy_grid')
    print(resultado)

def menu():
    cartelas = {}
    while True:
        print(tabulate([
            ['1', 'Gerar Cartelas'],
            ['2', 'Salvar Cartelas'],
            ['3', 'Ler Cartelas'],
            ['4', 'Imprimir Cartelas'],
            ['5', 'Sair']
        ], headers=['Opção', 'Descrição'], tablefmt='fancy_grid'))

        opcao = input('Escolha uma das opções: ').strip()

        if opcao == '1':
            gerar_str = input('Quantas cartelas deseja gerar? ').strip()
            try:
                gerar = int(gerar_str)  # Converte a entrada para inteiro
                if 1 <= gerar <= 10000:
                    sucesso, cartelas = GerarCartelas(gerar)
                    if sucesso:
                        print(f'\n{gerar} cartelas geradas!')
                        print('Próximo passo...')
                    else:
                        print(cartelas)
                    time.sleep(1)
                else:
                    print('Insira um número entre 1 e 10000.')
            except ValueError:
                print('Insira um número válido.')

        elif opcao == '2':
            if cartelas:
                SalvarCartelas(cartelas)
            else:
                print('Não foram geradas cartelas.')

        elif opcao == '3':
            cartelas = LerCartelas()
            if cartelas:
                print('Cartelas lidas com sucesso!')
                for numero_cartela, cartela in cartelas.items():
                    ImprimirCartelas(cartelas, numero_cartela)
            else:
                print('Não foram encontradas cartelas.')

        elif opcao == '4':
            numero_cartela = input('Informe o número da cartela para imprimir (ex: CART_000123): ').strip()
            ImprimirCartelas(cartelas, numero_cartela)
            print('Sorteio!')
            time.sleep(1)

        elif opcao == '5':
            print('Saindo...')
            break

        else:
            print('ERRO! Opção inválida. Tente novamente.')
            time.sleep(2)

try:
    menu()
except Exception as e:
    print('\nO programa deu o seguinte erro:', e)

