#questão 9 da lista 2 

import sys 

val = int(input("Informe um número inteiro positivo:"))

if val <= 0:
    print("Informe um valor válido!!!")
    sys.exit()

cont = val
contd = 0

while cont > 0:
    cont //= 10
    contd += 1

cont = val
soma = 0

while cont > 0:
    n = cont % 10
    cont //= 10
    soma += n ** contd

if soma == val:
    print(f"{val} É UM NÚMERO DE ARMSTRONG")
else:
    print(f"{val} NÃO É UM NÚMERO DE ARMSTRONG")





