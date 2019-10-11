velocidade = int(input('Digite a velocidade em Km/h que vc estava: '))
    
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Você foi multado em R$ {:.2f}. Sua velocidade foi {} Km/h.'.format(multa, velocidade))
else:
    print('Parabéns, vc está dentro do limite de velocidade')