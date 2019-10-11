nome = str(input('Digite o nome completo: ')).strip()

print('Seu nome em Maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em Minúscula é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separaNome = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separaNome[0], len(separaNome[0])))