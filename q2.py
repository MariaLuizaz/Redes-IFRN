#questão 2 da lista 2

import sys

num1 = int(input("Informe um número inteiro positivo:"))
num2 = int(input("Informe outro número inteiro positivo:"))

if num1 < 0 or num2 < 0:
    print("Informe números válidos!!!")
    sys.exit()

while num2 != 0:
    div = num1 % num2
    num1 = num2 
    num2 = div

print(f'O MDC entre os dois números é: {num1}')






