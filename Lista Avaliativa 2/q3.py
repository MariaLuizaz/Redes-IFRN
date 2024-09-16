#questão 3 da lista 2 

var1 = int(input("Informe n fatores primos que um número pode ter: "))

n = 0
n2 = 2

while n < var1:
    numero = n2
    primos = 0
    i = 2 

    while i * i <= numero:
        if numero % i == 0:
            primos += 1
            while numero % i == 0:
                numero //= i
        i += 1
    
    if numero > 1:
        primos += 1

    if primos == var1:
        print(n2)
        n += 1

    n2 += 1
