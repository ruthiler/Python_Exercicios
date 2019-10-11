'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)

print('''SUA OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Escolha uma: '))

print('JO---')
sleep(1)
print('KEN---')
sleep(1)
print('POOOO!!!')
print('-=' *13, end='')
print('-')
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))

if computador == 0:     # computador escolhe PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada INVÁLIDA. Tente novamente')

elif computador == 1:   # computador escolhe PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada INVÁLIDA. Tente novamente')

elif computador == 2:   # computador escolhe TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA. Tente novamente')

print('-=' *13, end='')
print('-')