print('--> Este programa calcula ângulos e classifica triângulos.')

a = float(input('Informe o primeiro comprimento de um lado do triângulo:'))
b = float(input('Informe o segundo comprimento:'))
c = float(input('Informe o terceiro comprimento:'))

if a == b + c or b == a + c or c == b + a:
    print('Não é possível formar um triângulo com esses lados!!')
    
import math 

angulo_a = math.degrees((a**2 + c**2 - b**2)) / (2 * a * c)
angulo_b = math.degrees((b**2 + c**2 - a**2)) / (2 * b * c)
angulo_c = (180 - a - b) 
print(f'Os três ângulos do triângulo são: {c:.2f}')

if a == b == c:
   print('Equilátero')
elif a == b or a == c or b == c:
    print('Isósceles ')
else:
    print('Escaleno')

if angulo_a > 90 or angulo_b > 90 or angulo_c > 90:
    print('Obtuso')
elif angulo_a == 90 or angulo_b == 90 or angulo_c == 90:
    print('Retângulo')
elif angulo_a < 90 or angulo_b < 90 or angulo_c < 90:
    print('Agudo')

