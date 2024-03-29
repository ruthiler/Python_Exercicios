# Desafio 081: Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    cont = ' '
    while cont not in 'SsNn':
        cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if cont in 'Nn':
        break
print('~' * 50)
print('Você digitou {} números.'.format(len(lista)))
lista.sort(reverse=True)
print('Os valores em ordem descrescente são {}'.format(lista))
if 5 in lista:
    print('O número 5 esta na lista!')
else:
    print('O número 5 não foi encontrado na lista!')