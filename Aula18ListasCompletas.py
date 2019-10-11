galera = list()
pessoa = list()
totmaior = totmenor = 0
for n in range(0, 3):
    pessoa.append(str(input('Digite o Nome: ')))
    pessoa.append(int(input('Digite a Idade: ')))
    galera.append(pessoa[:])
    pessoa.clear()

print('-=' * 20)
for p in galera:
    if p[1] >= 21:
        print('{} é maior de idade.'.format(p[0]))
        totmaior += 1
    else:
        print('{} é menor de idade'.format(p[0]))
        totmenor += 1

print('Temos {} maiores e {} menores de idade.'.format(totmaior, totmenor))