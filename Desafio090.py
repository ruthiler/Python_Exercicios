from typing import Dict

alunos = list()
aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['nota'] = float(input('A nota de {}: '.format(aluno['nome'])))
if aluno['nota'] >= 7:
    aluno['status'] = 'Aprovado'
else:
    aluno['status'] = 'Reprovado'
alunos.append(aluno.copy())
print(alunos)
print('mm')
