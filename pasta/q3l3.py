#questão 3 da lista 3 

import sys
import random

n = int(input('Insira um número entre 7 e 60: '))

if n < 7 or n > 60:
    print('Insira um número entre 7 e 60!!!')
    sys.exit()

lista = random.sample(range(1, 61), n)

valores = []

for tamanho in range(1, n + 1):
    indices = list(range(tamanho))
    while True:
        combinacao = [lista[i] for i in indices]
        valores.append(combinacao)
        
        for i in reversed(range(tamanho)):
            if indices[i] != i + len(lista) - tamanho:
                break
        else:
            break
        
        indices[i] += 1
        for j in range(i + 1, tamanho):
            indices[j] = indices[j - 1] + 1

with open('numeros_escolhidos.txt', 'w') as f:
    f.write(';'.join(map(str, lista)))

with open('combinacoes.txt', 'w') as f:
    for c in valores:
        f.write(';'.join(map(str, c)) + '\n')

qntd_v = len(valores)
print(f"Quantidade de combinações geradas: {qntd_v}")

combt = 2**n - 1
sena = 1 / combt if n >= 6 else 0
quina = 1 / combt if n >= 5 else 0
quadra = 1 / combt if n >= 4 else 0

print(f"Probabilidade de acertar a sena: {sena}")
print(f"Probabilidade de acertar a quina: {quina}")
print(f"Probabilidade de acertar a quadra: {quadra}")

