#questão1 lista 2 

import sys 

massa1 = float(input("Informe a massa inicial em gramas:"))

if massa1 <= 0:
    print("O valor da massa é inválido!!!")
    sys.exit()

tempo = 0
massa = massa1 

while massa > 0.5:
    massa/=2 
    tempo += 50

h = tempo // 3600
min = (tempo % 3600) // 60
seg = tempo % 60

print(f'A massa inicial é:{massa1} gramas')
print(f'A massa final é:{massa} gramas')
print(f'O tempo de decaímento foi de:{int(h)} horas, {int(min):02} minutos, {int(seg):02} segundos')

