# Desafio 058: Melhore o jogo do DESAFIO 028 onde o computador
# vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.
from random import randint

print('Olá, sou seu computador...\n'
      'Acabei de pensar em um numero entre 0 e 10.\n'
      'Você consegue adivinhar qual foi?')

computador = randint(0,10)
tentativas = 0
acertou = False

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if computador < jogador:
            print('Menos... tente novamente.')
        else:
            print('Mais... tente novamente. ')

print('\nParabéns, Acertou com {} tentativas.'.format(tentativas))
print('Eu pensei mesmo no {}.'.format(computador))



