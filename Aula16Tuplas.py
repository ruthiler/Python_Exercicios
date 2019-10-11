# Tupla = ()
# Lista = []
# Dicionário = {}

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(lanche)

print('\nFor direto na Tupla:')
for comida in lanche:
    print('Vou comer {}'.format(comida))

print('\nFor Usando Range e Len:')
for pos in range(0, len(lanche)):
    print('Vou comer {} da bandeja {}'.format(lanche[pos], pos))

print('\nFor usando o Enumerate direto na Tupla')
for pos, comida in enumerate(lanche):
    print('Vou comer {} da bandeja {}'.format(comida, pos))

print('\nSorted mostra a Tupla ordenada (Não modificou, apenas mostrou em ordem)')
print('Com Sorted {}'.format(sorted(lanche)))
print('Sem Sorted {}'.format(lanche))

a = (1, 5, 3, 8, 2)
b = (6, 7, 11, 15)
c = a + b
print('\nCom Sorted {}'.format(sorted(a)))
print('Sem Sorted {}'.format(a))
print('Soma da Tupla A + B = C -> {}'.format(c))