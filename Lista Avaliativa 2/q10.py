#questão 10 da lista 2

print("JOGO DA FORCA :)")

palavra_chave = "bacalhau"
palavra_chave = palavra_chave.upper()

palavra = len(palavra_chave)
chances = 6
certo = '_' * palavra
errado = ''

print("Palavra: " + ' '.join(certo))
print("Letras erradas: " + errado)
print(f"Chances restantes: {chances}")

while chances > 0 and '_' in certo:
    l = str(input("Insira uma letra: ").upper())

    if len(l) > 1:
       print("INSIRA APENAS UMA LETRA POR VEZ!!!")

    if l in certo or l in errado:
        print("Você já tentou essa letra.")
        continue

    if l in palavra_chave:
        certo2 = ''
        for i in range(palavra):
            if palavra_chave[i] == l:
                certo2 += l
            else:
                certo2 += certo[i]
        certo = certo2
    else:
        errado += l + ' '
        chances -= 1

    print("Palavra: " + ' '.join(certo))
    print("Letras erradas: " + errado)
    print(f"Chances restantes: {chances}")

if '_' not in certo:
    print("VOCÊ GANHOU!")
else:
    print("VOCÊ FOI ENFORCADO! A palavra era: " + palavra_chave)

