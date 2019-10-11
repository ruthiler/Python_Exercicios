# Desafio 062: Melhore o DESAFIO 061, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa encerrará quando ele disser
# que quer mostrar 0 termos.


print('-*-' *10)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
cont = 10
contador = 0
total = 0
while cont != 0:
    total += cont
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    cont = int(input('Quantos termos vc quer mostrar a mais? '))
print('PA finalizada com {} termos mostrados.'.format(total))


