# encoding: utf-8


# Desafio 084:Faça um programa que leia nome e peso de várias pessoas.
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

aluno = list()
turma = list()
totalcad = menor = maior = 0

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Peso: ')))
    turma.append(aluno[:])
    if len(turma) == 1:
        maior = menor = turma[0][1]
    else:
        if turma[-1][1] > maior:
            maior = turma[-1][1]
        if turma[-1][1] < menor:
            menor = turma[-1][1]
    aluno.clear()
    totalcad += 1
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Desaja continuar? [S/N] ')).strip().upper()[0]
    if cont in 'Nn':
        break

print('-=' * 40)
print('\nTemos {} pessoas cadastrasdas.'.format(totalcad))
print('O menor peso foi de {:.2f}Kg. Peso de'.format(menor), end=' ')
for p in turma:
    if p[1] == menor:
        print(p[0], end=' ')

print('\nO maior peso foi de {:.2f}Kg. Peso de'.format(maior), end=' ')
for p in turma:
    if p[1] == maior:
        print(p[0], end=' ')

print('\n')

# Outra forma
print('-=' * 40)
print('Colocando os leves e pesados em listas separadas.')
leve = list()
pesada = list()
for p in turma:
    if p[1] == menor:
        leve.append(p[0])
    if p[1] == maior:
        pesada.append((p[0]))

print('-=' * 40)
print('O menor peso foi de {:.2f}Kg. Peso de {}'.format(menor, leve))
print('O maior peso foi de {:.2f}Kg. Peso de {}'.format(maior, pesada))
