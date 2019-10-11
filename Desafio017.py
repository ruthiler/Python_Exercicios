from math import hypot

catAd = float(input('Digite o comprimento do Cateto Adjacente: '))
catOp = float(input('Digite o comprimento do Cateto Oposto: '))

hpt = hypot(catAd, catOp)

print('A hipotenusa é {}'.format(hpt))
