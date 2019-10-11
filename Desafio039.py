''' Exercício Python 039: Faça um programa que leia o ano de nascimento
    de um jovem e informe, de acordo com a sua idade, se ele ainda vai
    se alistar ao serviço militar, se é a hora exata de se alistar ou
    se já passou do tempo do alistamento. Seu programa também deverá
    mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

atual = date.today().year
nasc = int(input("Digite o ano do seu nascimento: "))
idade = atual-nasc
alist=18

if idade>alist:
    print("Você deveria ter se alistado a {} anos atrás".format(idade-alist))
elif idade<alist:
    print("Você só irá se alistar daqui a {} ano(s)".format(alist-idade))
elif idade==alist:
    print("Você deve se alistar esse ano")







