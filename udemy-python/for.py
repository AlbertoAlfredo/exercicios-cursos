# loop com listas e artigos
compras = ['arroz','feijão','macarrao','carne']
nome = 'joaquim'

for i in compras:
    print(i)

for i in nome:
    print(i)

print('####################################################')

#loop com somatório

vendas = [100,23,1234,9876]

total = 0

for i in vendas:
    total += i
print(total)

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

#loop com dicionarios

cores = {'verde': 'green', 'preto': 'black', 'azul': 'blue'}

for i in cores:
    print(i, ':', cores[i])
