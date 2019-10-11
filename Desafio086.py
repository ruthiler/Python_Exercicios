# Desafio 086: Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado. No final, mostre a matriz
# na tela com a formatação correta.

# encoding: utf-8
matriz = [[], [], []]

for n in range (0, 3):
    for i in range(0, 3):
        num = int(input('Digite um número para [{}][{}]: '.format(n, i)))
        matriz[n].append(num)

print('-=' * 30)
for n in range (0, 3):
    for i in range(0, 3):
        print('[  {}  ]'.format(matriz[n][i]), end='')
    print('')
