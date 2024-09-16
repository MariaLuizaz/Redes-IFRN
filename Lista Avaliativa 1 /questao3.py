print('--> Este programa calcula detalhes do desempenho de um veículo em uma viagem.')


tempohi = int(input('Informe a hora de partida:'))
tempomini = int(input('Informe os minutos de partida:'))
tempohf = int(input('Informe a hora de chegada:'))
tempominf = int(input('Informe os minutos de chegada:'))
descanso = int(input('Informe o tempo de parada para descanso em segundos:'))
combustivelg = float(input('Informe quantos litros de combustível foram gastos:'))
combustivelp = float(input('Informe o preço do litro de combustível:R$'))
distancia = float(input('Informe a distância percorrida em KM:'))

tempoi = tempohi * 3600 + tempomini * 60
tempof = tempohf * 3600 + tempominf * 60
tempo_de_viagem = (tempof - tempoi - descanso)
print(f'Tempo de viagem: {tempo_de_viagem} segundos')

tempo = (tempo_de_viagem + descanso) / 3600
velocidade_m_global = (distancia / tempo)
velocidade_m_mov = distancia / (tempo - descanso / 3600)
print(f'A velocidade média global é: {velocidade_m_global:.2f} Km/h')
print(f'A velocidade média em movimento é: {velocidade_m_mov:.2f} Km/h')

custocombust = (combustivelg * combustivelp)
print(f'O custo do combustível foi de:R${custocombust:.2f}')

print('Quanto ao desempenho do carro:')
kmporl = (distancia / combustivelg)
print(f'Em KM por litros: {kmporl:.2f} Km/l')
litrosporh = combustivelg / (tempo_de_viagem / 3600)
print(f'Em litros por hora: {litrosporh:.2f} l/h')
precopkm = (combustivelg / distancia)
print(f'Em preço por KM:R$ {precopkm:.2f}/Km')










