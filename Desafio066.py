# Desafio 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a
# condição de parada. No final, mostre quantos números foram digitados
# e qual foi a soma entre elas (desconsiderando o flag).

soma = cont = num = 0

while True:
    num = int(input('Digite um úmero [999 para SAIR]: '))
    if num == 999:
        break
    soma += num
    cont += 1

print('A soma dos {} número(s) digitados é {}.'.format(cont, soma))
print('FIM')

