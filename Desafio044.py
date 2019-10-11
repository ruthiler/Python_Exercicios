'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

preco = float(input('Qual o Valor da sua compra? '))

print('''ESCOLHA A FORMA DE PAGAMENTO
[ 1 ] À VISTA (DINHEIRO OU CHEQUE)
[ 2 ] À VISTA NO CARTÃO
[ 3 ] PARCELADO 2X NO CARTÃO
[ 4 ] PARCELADO 3 OU MAIS VEZES NO CARTÃO
''')
pag = int(input('Escolha a opção: '))
if pag == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R$ {:.2f}, terá um desconto de R$ {:.2f}. Total R$ {:.2f}'.format(preco, (preco-total), total))
elif pag == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de R$ {:.2f}, terá um desconto de R$ {:.2f}. Total R$ {:.2f}'.format(preco, (preco - total), total))
elif pag == 3:
    parc = preco/2
    print('Sua compra de {:.2f}, parcelado em 2x de {:.2f}'.format(preco, parc))
elif pag == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parc = total / totparc
    print('Sua compra de R$ {:.2f}, com juros de R$ {:.2f}'.format(preco, (total-preco)))
    print('Parcelado em {}x de {:.2f}. Total de R$ {:.2f}'.format(totparc, parc, total))
else:
    print('Opção errada. Tenta novamente.')
