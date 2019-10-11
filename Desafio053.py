# Desafio 053: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.


frase=str(input("Digite uma frase: ")).strip().upper()
separa = frase.split()
junto = ''.join(separa)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um PALÍDROMO.')
else:
    print('Não temos um PALÍDROMO.')

print('{} -> {}'.format(junto, inverso))