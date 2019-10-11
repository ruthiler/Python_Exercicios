# encoding: utf-8
# Desafio 087: Aprimore o desafio 086, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matriz = [[], [], []]
maior = somapar = somaterc = 0
for n in range (0, 3):
    for i in range(0, 3):
        matriz[n].append(int(input('Digite um número para [{}][{}]: '.format(n, i))))
        if matriz[n][i] % 2 == 0:
            somapar += matriz[n][i]
        if i == 2:
            somaterc += matriz[n][i]
        if n == 1:
            if matriz[n][i] > maior:
                maior = matriz[n][i]

print('-=' * 30)
for n in range (0, 3):
    for i in range(0, 3):
        print('[  {}  ]'.format(matriz[n][i]), end='')
    print('')

print('-=' * 30)
print('A soma de todos os valores pares: {}'.format(somapar))
print('A soma do valores da terceira coluna: {}'.format(somaterc))
print('O maior valor da segunda linha: {}'.format(maior))


