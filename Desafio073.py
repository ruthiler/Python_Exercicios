# Desafio 073: Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

brasileirao = ('Atletico', 'Flamengo', 'Corinthians', 'Palmeiras',
               'Fluminense', 'America-MG', 'Sao Paulo', 'Gremio',
               'Vasco da Gama', 'Internacional', 'Botafogo',
               'Sport Recife', 'Cruzeiro', 'EC Vitoria',
               'Santos', 'Chapecoense', 'Atletico-PR',
               'Bahia', 'Ceara SC','Parana')
print('-' * 30)
print('{:^30}'.format('Brasileirão'))
print('-' * 30)

print('Os Times são:')
for pos, time in enumerate(brasileirao):
    print('{:2}º - {}'.format(pos+1, time))

print('-' * 30)
print('Os 5 primeiros são:')
for pos, time in enumerate(brasileirao[0:5]):
    print('{}º - {}'.format(pos+1, time))

print('-' * 30)
print('Os últimos 4 são:')
for pos, time in enumerate(brasileirao[-4:]):
    print('{}º - {}'.format(pos+17, time))

print('-' * 30)
print('Times em Ordem Alfabética: ')
for time in sorted(brasileirao):
    print('{}'.format(time))

print('-' * 30)
print('O Chapecoense está na {}ª posição.'.format(brasileirao.index('Chapecoense')+1))