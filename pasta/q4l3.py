#questão 4 da lista 3 

import sys
import random

n = int(input('Informe a quantidade de elementos na lista:'))

if n < 0:
    print('Insira um valor positivo!!!')
    sys.exit()

lista = []

lista = [random.randint(0, 100) for i in range(n)]
print(f'lista: {lista}')

#media
media = sum(lista) / len(lista)
print(f"Média dos valores: {round(media, 1)}")

#mediana
lista2 = sorted(lista)
if n % 2 == 1:
    mediana = lista2[n // 2]
else:
    n1 = lista2[n // 2 - 1]
    n2 = lista2[n // 2]
    mediana = (n1 + n2) / 2
    print(f"Mediana dos valores: {mediana} ")

#variancia
som_quad = sum((x - media) ** 2 for x in lista)
var = som_quad / n
print(f"Variância populacional: {round(var, 1)}")

#desvio padrão
desv_pad = var ** 2 
print(f"Desvio-padrão populacional: {round(desv_pad, 1)}")



