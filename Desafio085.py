# Desafio 085: Crie um programa onde o usuário possa digitar sete valores
# númericos e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente

# encoding: utf-8

numeros = [[], []]
for n in range(1, 8):
    num = int(input('0{}º número: '.format(n)))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()
print('-=' * 35)
print('Os valores pares digitados foram: {}'.format(numeros[0]))
print('Os valores ímpares digitados foram: {}'.format(numeros[1]))