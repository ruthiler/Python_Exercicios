frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('O primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('O última letra A apareceu na posição {}'.format(frase.rfind('A')+1))