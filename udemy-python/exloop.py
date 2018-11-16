repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco do produto: '))
    fatura.append([produto,preco])
    total += preco
    repetir = input('Deseja comprar mais algum produdo? s/n  ').lower()

for i in fatura:
    print(i[0], ': ', i[1])
print('O total da fatura é: ' , total)
