# Desafio 072: Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa deverá
# ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
from time import sleep

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        pos = int(input('Digite um número para escrever por extenso: [0 a 20] '))
        if 0 <= pos <=20:
            break
        else:
            print('Tente novamente.')
    print('{} -> {}'.format(pos, num[pos]))
    sleep((0.5))
    cont = str(input('Desaja continuar? [S ou N] ')).strip().upper()[0]
    if cont in 'N':
        break
print('Finalizando')