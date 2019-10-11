# Desafio 082: Crie um programa que vai ler vários números e colocar
# em uma lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
impares = []

while True:
    num = (int(input('Digite um número: ')))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    cont = ' '
    while cont not in 'SnNn':
        cont = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if cont in 'Nn':
        break
#for n in lista:
#    if n % 2 == 0:
#        pares.append(n)
#    else:
#        impares.append(n)
print('~' * 40)
print('~' * 40)
print('A Lista completa é {}'.format(lista))
print('A Lista de pares é {}'.format(pares))
print('A Lista de ímpares é {}'.format(impares))

