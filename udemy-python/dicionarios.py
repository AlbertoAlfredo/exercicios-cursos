cores = {'blue':'azul', 'red':'vermelho', 'bown':'marrom', 'yellow':'amarelo'}

cor = input('Digite uma cor para tradução: ')
print(cores.get(cor, 'Essa cor não está no banco de dados'))
