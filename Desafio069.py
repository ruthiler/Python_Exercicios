# Desafio  069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
# não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maior18 = homem = mulher20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    cont = ' '
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':                                 # Validar sexo somente com S ou N
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 20)
    while cont not in 'NS':                                 # Validar Continue somente com S ou N
        cont = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    if cont in 'Nn':
        break
print('{} pessoas com mais de 18 anos.'.format(maior18))
print('{} homens cadastrados'.format(homem))
print('{} mulheres com menos de 20 anos'.format(mulher20))
