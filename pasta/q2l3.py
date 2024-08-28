#questão2 da lista 3 

import sys 

x = int(input("Informe a quantidade de elementos na lista: "))
n = int(input('Insira um número ou 0 para parar:'))

números = []

números.append(n)

while n != 0:
    números.sort() 
    print(f"números: {números}")

    n = input("Insira um valor: ")
    n = int(n)
    
    if len(números) < x: 
        números.append(n)

    else:
        contador = 0
        for i in números:  
            if n < i:
                números[contador] = n
                print(f'números: {números}')
                break
            contador =+ 1 

print(números)
    
    
    