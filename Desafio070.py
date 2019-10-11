# Desafio 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = produtomil = menor = 0
print('~' * 50)
print('{:-^50}'.format('COMPRAS'))
print('~' * 50)

while True:
    produto = str(input('Nome do Produto: ')).strip()
    valor = float(input('Valor: R$ '))
    total += valor
    if valor > 1000:
        produtomil += 1
    if menor == 0:
        menor = valor
        menorproduto = produto
    if valor < menor:
        menor = valor
        menorproduto = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
print('~' * 50)
print('O total de compras foi {:.2f}'.format(total))
print('{} produtos custam mais de R$ 1000,00'.format(produtomil))
print('O produto mais barato foi {} custando R$ {:.2f}.'.format(menorproduto, menor))
print('{:-^50}'.format('FIM DO PROGRAMA'))