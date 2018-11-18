l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
print('A área da parede é {:.2f}m², são necessários {} litros de tinta'.format(area, area / 2))