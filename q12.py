#questão 12 da lista 2 

m = str(input("Insira uma mensagem para criptografar: "))
chave = str(input("Insira a chave: "))

mcripto = ""
chave1 = 0
chave2 = len(chave)

for i in m:
    if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
        desloc = ord(chave[chave1 % chave2].upper()) - ord('A')
        var1 = ord('a') if 'a' <= i <= 'z' else ord('A')
        
        icripto = chr((ord(i) - var1 + desloc) % 26 + var1)
        mcripto += icripto
        
        chave1 += 1
    else:
        mcripto += i

print(f"Mensagem criptografada: {mcripto}")

mdescripto = ""
chave1 = 0

for i in mcripto:
    if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
        desloc = ord(chave[chave1 % chave2].upper()) - ord('A')
        var1 = ord('a') if 'a' <= i <= 'z' else ord('A')
        
        idescripto = chr((ord(i) - var1 - desloc) % 26 + var1)
        mdescripto += idescripto
        
        chave1 += 1
    else:
        mdescripto += i

print(f"Mensagem descriptografada:{mdescripto}")