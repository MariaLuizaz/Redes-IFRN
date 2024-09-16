#questão 5 da lista 2 

import sys 

valor = int(input("Informe um valor inteiro positivo:"))

if valor <= 0:
    print("Este não é um valor válido!!!")
    sys.exit()

c = 0

while valor > 0:
    c += 1 
    valor //= 10

print(f"O número possui: {c} digítos")
