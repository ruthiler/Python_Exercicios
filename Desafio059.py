# Desafio Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

sair = False

while not sair:

    print('- ' * 15)
    print('''        [ 1 ] somar 
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa''')
    menu = int(input('>>>>>>> Qual a sua opção: '))
    print('- ' * 15)
    if menu == 1:
        print('>>>>>>> {} + {} = {}'.format(num1, num2, num1+num2))
    elif menu == 2:
        print('>>>>>>> {} X {} = {}'.format(num1, num2, num1*num2))
    elif menu == 3:
        if num1 > num2:
            print('>>>>>>> {} é maior que {}'.format(num1, num2))
        else:
            print('>>>>>>> {} é maior que {}'.format(num2, num1))
    elif menu == 4:
        print('Quais são os novos número?')
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
    elif menu == 5:
        sair = True
    else:
        print('Opção INVÁLIDA. Tente novamente')

print('FIM!')