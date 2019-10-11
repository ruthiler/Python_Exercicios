num = int(input('Digite um numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A Unidade é {}'.format(u))
print('A Dezena é {}'.format(d))
print('A Centena é {}'.format(c))
print('A Milhar é {}'.format(m))

