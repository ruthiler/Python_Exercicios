# Desafio 078: Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi o maior e
# o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = 0
for n in range(0, 5):
    lista.append(int(input('Digite o valor p posição {}: '.format(n))))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
# menor = min(lista)
# maior = max(lista)
print('O menor valor digitado foi {} na posição '.format(menor), end='')
for ind, valor in enumerate(lista):
    if valor == menor:
        print('{} '.format(ind), end='')
print('\nO maior valor digitado foi {} na posição '.format(maior), end='')
for ind, valor in enumerate(lista):
    if valor == maior:
        print('{} '.format(ind), end='')
