print('--> Este programa calcula um intervalo de tempo entre duas datas.')

dia1 = int(input('Informe o dia inicial:'))
mes1 = int(input('Informe o mês inicial:'))
dia2 = int(input('Informe o dia final:'))
mes2 = int(input('Informe o mês final:'))


if dia1 > dia2 and mes1 > mes2 or mes1 == mes2:
    print('Data inválida!! A data inicial não pode ser maior que a data final!!')

janeiro = 31
fevereiro = 28
março = 31
abril = 30
maio = 31 
junho = 30
julho = 31
agosto = 31
setembro = 30
outubro = 31
novembro = 30
dezembro = 31 

quant_dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dias_dt1 = sum(quant_dias_mes[:mes1 - 1]) + dia1  
dias_dt2 = sum(quant_dias_mes[:mes2 - 1]) + dia2 

intervalo = (dias_dt2- dias_dt1)
print(f'O número de dias entre as duas datas é: {intervalo:.0f}')
