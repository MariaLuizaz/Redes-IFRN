#questão 7 da lista 2 

import sys 

var1a = int(input("Informe um valor inteiro inicial:"))
rpa = float(input("Informe a razão da P.A:"))

quant_a = int(input("Informe a quantidade de elementos da P.A:"))

if quant_a <= 0:
    print("inválido!!!")
    sys.exit()

soma = 0
valor = var1a

print("Valores da P.A:")
for i in range(quant_a):
    print(valor)
    soma += valor
    valor += rpa

print(f"Soma da P.A: {soma}") 

if rpa == 0:
    print("A P.A É CONSTANTE")
elif rpa > 0:
    print("A P.A É CRESCENTE")
else:
    print("DECRESCENTE")

ppa = int(input("Informe um  valor inteiro n correspondente a enésima posição de um elemento da P.A:"))

if ppa <= 0:
    print("Insira uma posição válida!!!")

valorp = var1a + (ppa - 1) * rpa
print(f"O valor na posição {ppa} é: {valorp}")