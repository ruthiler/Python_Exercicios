#Desafio 050: Desenvolva um programa que leia seis numeros inteiros
#e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
contador = 0

for cont in range(1, 7):
    num = int(input('Digite o {} numero: '.format(cont)))
    if num % 2 == 0:
        soma += num
        contador += 1

print('Voce digitou {} numero pares e a soma deles e {}'.format(contador, soma))
