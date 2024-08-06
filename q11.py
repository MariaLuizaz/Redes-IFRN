#questão 11 da lista 2 


print("JOGO DO ROBÔ :)")

x = str(input("insira a posição inicial do robô (coordenada x):"))
y = str(input("Insira a posição inicial do robô (coordenada y):"))

x = int(x)
y = int(y)

movimentos = str(input("Insira comandos de movimento (U (cima); D (baixo); R (direita); L (esquerda); O (noroeste, cima-esquerda); N (nordeste, cima-direita); E (sudeste, baixo-direita); W (sudoeste, baixo-esquerda):")).upper()

m = 0
mov = ''

for movimento in movimentos:
    if movimento == 'U':
        y += 1
        m += 1
        mov += 'U'
    elif movimento == 'D':
        y -= 1
        m += 1
        mov += 'D'
    elif movimento == 'R':
        x += 1
        m += 1
        mov += 'R'
    elif movimento == 'L':
        x -= 1
        m += 1
        mov += 'L'
    elif movimento == 'O':
        x -= 1
        y += 1
        m += 1
        mov += 'O'
    elif movimento == 'N':
        x += 1
        y += 1
        m+= 1
        mov += 'N'
    elif movimento == 'E':
        x += 1
        y -= 1
        m += 1
        mov += 'E'
    elif movimento == 'W':
        x -= 1
        y -= 1
        m += 1
        mov += 'W'

if int(x) > 0 and int(y) > 0:
    quad1 = "Primeiro Quadrante"
elif int(x) < 0 and int(y) > 0:
    quad1 = "Segundo Quadrante"
elif int(x) < 0 and int(y) < 0:
    quad1 = "Terceiro Quadrante"
elif int(x) > 0 and int(y) < 0:
    quad1 = "Quarto Quadrante"
else:
    quad1 = "Eixo x ou Eixo y"

if x > 0 and y > 0:
    quad2= "Primeiro Quadrante"
elif x < 0 and y > 0:
    quad2 = "Segundo Quadrante"
elif x < 0 and y < 0:
    quad2 = "Terceiro Quadrante"
elif x > 0 and y < 0:
    quad2 = "Quarto Quadrante"
else:
    quad2= "Eixo X ou Eixo Y"

print(f"Posição inicial: x = {x}, y = {y}")
print(f"Posição final: x = {x}, y = {y}")
print(f"Quantidade de movimentos válidos executados: {m}")
print(f"Movimentos válidos executados: {mov}")
print(f"Quadrante que iniciou: {quad1}")
print(f"Quadrante que terminou: {quad2}")





