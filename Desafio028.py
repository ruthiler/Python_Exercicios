from random import randint

print('Eu pensei em um número entre 0 e 5, tente acertar qual eu pensei:')
num = int(input('Digite um Número entre 0 e 5: '))

x = randint(0,5)

if num == x:
    print('Você venceu, eu pensei mesmo no {}'.format(x))
else:
    print('Você perdeu, eu não pensei no {}'.format(num))

