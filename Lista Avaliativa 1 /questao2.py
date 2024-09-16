print('--> Este programa calcula a quantidade de cédulas e moedas de um saque em um caixa eletrônico.')

valor = float(input('Informe o valor do saque:R$'))

if valor <= 0:
    print('Este valor é inválido!!')
else:
    cem = valor // 100
    valor -= cem * 100
    cinquenta = valor // 50
    valor -= cinquenta * 50
    vinte = valor // 20
    valor -= vinte * 20
    dez = valor // 10
    valor -= dez * 10
    cinco = valor // 5 
    valor -= cinco * 5
    dois = valor // 2
    valor -= dois * 2
    um = valor // 1 
    valor -= um * 1 
    cinqcents = valor // 0.50
    valor -= cinqcents * 0.50
    vintecinco = valor // 0.25
    valor -= vintecinco * 0.25
    dezcents = valor // 0.10
    valor -= dezcents * 0.10
    cincocents = valor // 0.5
    valor -= cincocents * 0.5
    umcents = valor // 0.01
    valor -= umcents * 0.01

    
if cem > 0:
    print(f'{cem} cédula(s) de cem')
if cinquenta > 0:
    print(f'{cinquenta} cédula(s) de cinquenta')
if vinte > 0:
    print(f'{vinte} cédula(s) de vinte')
if dez > 0:
     print(f'{dez} cédula(s) de dez')
if cinco > 0:
    print(f'{cinco} cédula(s) de cinco')
if dois > 0:
    print(f'{dois} cédula(s) de dois')
if um > 0:
    print(f'{um} moeda(s) de um real')
if cinqcents > 0:
    print(f'{cinqcents} moeda(s) de cinquenta centavos')
if vintecinco > 0:
    print(f'{vintecinco} moeda(s) de vinte e cinco centavos')
if dezcents > 0:
    print(f'{dezcents} moeda(s) de dez centavos')
if cincocents > 0:
    print(f'{cincocents} moeda(s) de cinco centavos')
if umcents > 0:
    print(f'{umcents} moeda(s) de um centavos')






