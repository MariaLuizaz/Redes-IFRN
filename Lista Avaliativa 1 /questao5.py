print('--> Este programa calcula o valor do pagamento em um estacionamento.')


tempomin = int(input('Informe o tempo de permanência do carro em minutos:'))


if tempomin <= 60:
   taxa = 8.00
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 61 and tempomin <= 120:
   taxa = (8.00 + 8.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 121 and tempomin <= 180:
   taxa = (5.00 + 16.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 181 and tempomin <= 240:
   taxa = (10.00 + 16.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin == 300:
   taxa = (16.00 + 10.00) + (3.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 301 and tempomin <=360:
   taxa = (16.00 + 10.00) + (6.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 361 and tempomin <= 480:
   taxa = (16.00 + 10.00) + (9.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 481 and tempomin <= 540:
   taxa = (16.00 + 10.00) + (12.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 541 and tempomin <= 600:
   taxa = (16.00 + 10.00) + (15.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 601 and tempomin <= 660:
   taxa = (16.00 + 10.00) + (18.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 661 and tempomin <= 719:
   taxa = (16.00 + 10.00) + (21.00)
   print(f'Valor a ser pago:R$ {taxa:.2f}')
elif tempomin >= 720:
   taxa = 30.00
   print(f'Valor a ser pago:R$ {taxa:.2f}')




