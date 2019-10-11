# Desafio 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
from time import sleep
print('=' * 35)
print('{:^35}'.format('BANCO RUTHILER'))
print('=' * 35)
valor = int(input('Qual o valor para sacar? '))
total = valor
ced = 50
totalced = 0
print('Calculando...')
sleep(0.5)
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print('Total de {} cédulas de {}.'.format(totalced, ced))
            sleep(0.5)
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('{:=^35}'.format('VOLTE SEMPRE'))
