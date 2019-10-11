dias=float(input('Por quantos dias o carro foi alugado? '))
km=float(input('Quantos quilometros foram percorridos? '))

valorDia = dias*60
valorKm = km*0.15
total = valorDia+valorKm

print('O Valor total do aluguel foi R$ {:.2f}'.format(total))
