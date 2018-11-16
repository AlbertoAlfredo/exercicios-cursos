mes=('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

nascimento = input('Digite a data do seu nascimento no formato DD/MM/AAAA \n')
mes_nascimento = int(nascimento[3:5])-1
print('Você nasceu no mes de',mes[mes_nascimento])
