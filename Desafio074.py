# Desafio 074: Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os número soteados foram: ', end='')
for n in numeros:
    print('{} '.format(n),  end='')

print('\n\n{:-^40}'.format('Maior e menor usando o SORTED'))
print('O menor valor sorteado foi {}.'.format(sorted(numeros)[0]))
print('O maior valor sorteado foi {}.'.format(sorted(numeros)[-1]))

print('\n{:-^40}'.format('Maior e menor usando MAX e MIN'))
print('O menor valor sorteado foi {}.'.format(min(numeros)))
print('O maior valor sorteado foi {}.'.format(max(numeros)))



