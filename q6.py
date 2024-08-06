#questão 6 da lista 2 

import sys 

var1 = int(input("Informe um valor inteiro inicial:"))
r = float(input("Informe a razão da P.G:"))

quant = int(input("Informe a quantidade de elementos da P.G:"))

if quant <= 0:
    print("inválido!!!")
    sys.exit()

soma = 0
valor = var1 

print("Valores da P.G:")
for i in range(quant):
    print(valor)
    soma += valor
    valor *= r

print()
print(f"Soma da P.G: {soma}")

if r > 1:
    print("A PG É CRESCENTE")
elif r < -1:
    print("A PG É DECRESCENTE")
elif r == 1:
    print("A PG É CONSTANTE")
else:
    print("A PG É OSCILANTE")

p = int(input("Informe um  valor inteiro n correspondente a enésima posição de um elemento da P.G:"))

if p < 0:
    print("Insira uma posição válida!!!")
    sys.exit()

valorp = var1 * (r ** (p - 1))
print(f"O valor na posição {p} é: {valorp}")







    



