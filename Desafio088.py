# encoding: utf-8
# Desafio 088: Faça um programa que ajude um jogador da Mega Sena a
# criar palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.

from random import randint
from time import sleep
jogos = list()
palpite = list()
print('-' * 33)
print('{:^33}'.format('JOGOS PARA A MEGA SENA'))
print('-' * 33)
numjogo = int(input('Quantos jogos você quer? '))
for n in range(0, numjogo):
    while len(palpite) < 6:
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()

print('\n{:~^33}\n'.format('SORTEANDO {} JOGOS'.format(numjogo)))
c = 1
for p in jogos:
    sleep(1)
    print('Jogo {}: {}'.format(c, p))
    c += 1


