# Desafio 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    print('~' *38)
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for cont in range (1, 11):
        print('{:2} X {:2} = {:2}'.format(num, cont, num*cont))
print('Programa de tabuada encerrado. Volte sempre!')