'''Desafio 049: Refaca o DESAFIO 009, mostrando a tabuada de um nimero
que o usuario escolher, so que agora utilizando um laco for.'''

tab=int(input('Digite um numero para ver sua tabuada: '))

for cont in range(1, 11):
    print('{} x {:2} = {}'.format(tab, cont, tab*cont))
print('Fim')
