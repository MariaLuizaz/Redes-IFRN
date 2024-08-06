#questão 4 da lista 2 

valor = 1

while valor < 1000000:
    if valor % 2 == 0 or valor % 5 == 0:
        soma = (valor // 100000 % 10) ** 5 + (valor // 10000 % 10) ** 5 + (valor // 1000 % 10) ** 5 + (valor // 100 % 10) ** 5 + (valor // 10 % 10) ** 5 + (valor % 10) ** 5

        if soma == valor:
            print(valor)

    valor += 1