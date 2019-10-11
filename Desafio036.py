casa = float(input('Qual o Valor da casa: '))
salario = float(input('Qual o valor de Salário: '))
anos = float(input('Quantos anos de financiamento: '))
mensalidade = (casa / (anos*12))

if mensalidade > (salario*0.30):
    print('Emprestimo negado')
else:
    print('Emprestimo Concedido')
    print('Valor da mensalidade {} paga em {} meses'.format(mensalidade, (anos*12)))
