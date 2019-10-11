# Desafio 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-*-' *10)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
while termo < (razao*10):
    print(' {}'.format(termo), end=' ->')
    termo = termo + razao
print(' FIM')
