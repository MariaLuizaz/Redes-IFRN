print('--> Este programa calcula e exibe a data de aposentadoria.')

import sys
from datetime import datetime, timedelta

sexo = input('Informe seu sexo (masculino / feminino):')
if sexo == 'masculino':
    idade = 65
    aposentadoria = 35 
elif sexo == 'feminino':
    idade = 62
    aposentadoria = 30
else:
    print('sexo inválido!!')
    sys.exit()

data_nascimento = (input('Informe sua data de nascimento no formato DD/MM/AAAA:'))
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
data_contprev = (input('Informe a data do início de contribuição DD/MM/AAAA:'))
data_contprev = datetime.strptime(data_contprev, '%d/%m/%Y')

idade_atual = datetime.now().year - data_nascimento.year 
tempo_contribuição = (datetime.now() - data_contprev).days / 365 

if idade_atual > idade and tempo_contribuição > aposentadoria:
    print('Parabéns, você pode se aposentar!!')

data_aposentadoria = data_nascimento + timedelta(days= idade * 365)
data_contribuicao = data_contprev + timedelta(days= aposentadoria * 365)
dt_ap = max (data_aposentadoria, data_contribuicao)
print(f'Data de aposentadoria: {data_aposentadoria.strftime('%d/%m/%Y')}')







