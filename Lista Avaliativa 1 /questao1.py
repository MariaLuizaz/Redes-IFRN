print('--> Este programa calcula a soma dos algarismos de um número de até 4 digitos.')

número = int(input('Digite um número:'))

if número < 0 or número > 9999:
    print('Este número é inválido!!') 

else:
 uni = número // 1 % 10
 dez = número // 10 % 10
 cen = número // 100 % 10
 mil = número // 1000 % 10

result = (uni + dez + cen + mil)

print(f'A soma dos algarismos é: {result:.0f}')


