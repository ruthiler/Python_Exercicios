# Desafio 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep
venc = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 10)
    soma = jogador + computador
    aposta = ' '
    while aposta not in 'PpIi':
        aposta = str(input('Par ou Ímpar? [P OU I] ')).strip().upper()[0]
    sleep(1)
    print('Você jogou {} e o computador {}. Total de {}.'.format(jogador, computador, soma))
    if soma % 2 == 0 and aposta == 'P':
        print('Parabéns. Você apostou PAR e ganhou.')
        venc += 1
    elif soma % 2 == 1 and aposta == 'I':
        print('Parabéns. Você apostou ÍMPAR e ganhou.')
        venc += 1
    else:
        print('Que pena, você perdeu.')
        break
    print('Vamos joga novamente...')
    print('~' *45)
print('~' *45)
print('GAME OVER. Você ganhou {} vezes.'.format(venc))

