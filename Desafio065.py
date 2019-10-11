# Desafio 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior
# e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

continuar = 'S'
total = contador = maior = menor = 0
while continuar != 'N':
    num = int(input('Digite um número: '))
    if contador == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    total += num
    contador += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
media = total / contador
print('A média dos {} números digitados é {}.'.format(contador, media))
print('{} é o menor número e {} é o maior número.'.format(menor, maior))