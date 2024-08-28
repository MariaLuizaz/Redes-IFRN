#questão1 lista 3 

import sys 
import random

l = int(input('Informe a número de linhas da matriz:'))
c = int(input('Informe o número de colunas da matriz:'))

if l <= 0 or c <= 0:
    print('informe um número válido')
    sys.exit()

matriz = list()

matriz = [[random.randint(1, 9) for i in range(l)] for i in range(c)]

print('Matriz original:')
for l in matriz:
    print(l)

matriz_tp = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print('Matriz transposta:')
for l in matriz_tp:
    print(l)


