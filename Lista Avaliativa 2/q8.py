#questão 8 da lista 2 

import sys 

num = int(input("Informe um número inteiro positivo:"))

if num <= 0:
    print("Informe um número válido!!!")
    sys.exit()

n = 1 
positivo = 1 

while positivo < num:
    n += 1
    positivo = n * (n + 1) // 2

if positivo == num:
    print(f"{num} É TRIANGULAR")
else:
    print(f"{num} NÃO É TRIANGULAR")
