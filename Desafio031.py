distancia = int(input('Qual a distância da viagem: '))

if distancia <= 200:
    preco = distancia * 0.50
    print('A Passagem custa R$ {:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('A Passagem custa R$ {:.2f}'.format(preco))