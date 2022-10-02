altura = float(input('Qual a altura da sua parede?'))
largura = float(input('Qual a largura da sua parede?'))

area = altura * largura

pintura = area / 2

print('sua parede possui {:.0f} metros quadrados.'.format(area))
print('Você vai precisar de {:.0f} Litros de tinta para pintar a parede'.format (pintura))