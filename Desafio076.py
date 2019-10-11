# Desafio 076: Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.60,
            'Caneta', 1.80,
            'Compasso', 7.50,
            'Mochila', 66.00,
            'Livro', 80.00)
print('-' * 39)
print('{:~^39}'.format('LISTAGEM DE PRODUTOS'))
print('-' * 39)
for n in range(0, len(produtos)):
    if n % 2 == 0:
        print('{:.<30}'.format(produtos[n]), end='')
    else:
        print('R$ {:>6.2f}'.format(produtos[n]))