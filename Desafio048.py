'''Desafio 048: Faça um programa que calcule a soma entre todos
os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

soma=0
contador=0
for cont in range (1, 501, 2):
    if cont%3 == 0:
        #print(cont)
        soma=soma+cont
        contador=contador+1
print('A soma dos {} números e igual a {}'.format(contador,soma))

# ou entao

soma=0
contador=0
for cont in range (1, 501):
    if cont%3 == 0 and cont%2!=0: #Verifica se é multiplo de 3 e impar
        #print(cont)
        soma=soma+cont
        contador=contador+1
print('A soma dos {} números e igual a {}'.format(contador,soma))
