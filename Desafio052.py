#Exercicio Python 052: Faca um programa que leia um numero inteiro
# e diga se ele e ou nao um numero primo.

numero = int(input('Digite um numero: '))
cont = 0
for c in range (1, numero+1):
    if numero % c == 0:
        cont += 1

if cont == 2:
    print('{} e primo'.format(numero))
else:
    print('{} nao e primo'.format(numero))

