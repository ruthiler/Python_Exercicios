# encoding: utf-8
from time import sleep

alunos = list()
notas = list()
aluno = list()

while True:
    aluno.append(str(input('Nome: ')).title())
    notas.append(int(input('Nota 1: ')))
    notas.append(int(input('Nota 2: ')))
    aluno.append(notas[:])
    aluno.append(float((notas[0] + notas[1]) / 2))
    alunos.append(aluno[:])
    notas.clear()
    aluno.clear()
    cont = ' '
    while cont not in 'NnSs':
        cont = str(input('Deseja Continuar? [S/N] '))
    if cont in 'Nn':
        break

print('=' * 45)
print('{:<3} {:<35} {:^5}'.format('No.', 'NOME', 'MÉDIA'))
for i, a in enumerate(alunos):
    print('{:<3} {:<35} {:^5}'.format(i, a[0], a[2]))

while True:
    print('=' * 45)
    escolha = 0
    escolha = int(input('Mostrar notas de qual aluno? [999 p/ Sair]: '))
    if escolha == 999:
        print('=' * 45)
        print('FINALIZANDO...')
        sleep(1)
        break
    if escolha < len(alunos):
        print('As notas de {} são {}.'.format(alunos[escolha][0], alunos[escolha][1]))
    else:
        print('O Aluno não existe. Tente novamente.')

print('<<<< VOLTE SEMPRE >>>>')