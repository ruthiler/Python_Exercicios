# Desafio  079: Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado! Não vou adicionar....')
    cont=' '
    while cont not in 'NSns':
        cont=str(input('Desaja continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        break
lista.sort()
print('{:~^36}'.format('FINALIZANDO'))
print('Você adicionaou os números {}'.format(lista))
