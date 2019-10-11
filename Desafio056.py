# Desafio 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do
# homem mais velho e quantas mulheres têm menos de 20 anos.

total = 0
maioridade = 0
velho = ''
mulher20 = 0
for p in range( 1, 5 ):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).upper().strip()

    total += idade
    if sexo == 'M' and idade>maioridade:
        maioridade = idade
        velho = nome
    if sexo == 'F' and idade<20:
        mulher20 += 1

mediaidade = total/4
print('A média de idade das 4 pessoas é {}'.format(mediaidade))
print('O homem mais velhor é {} com {} anos'.format(velho, maioridade))
print('Entre as 4 pessoas, existe {} mulheres com menos de 20 anos'.format(mulher20))