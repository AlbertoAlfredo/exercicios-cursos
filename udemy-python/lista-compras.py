repetir = 's'
fatura = []
total = 0
valida_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    
    while valida_preco == False:
        preco = input('Digite o preco do produto: ')
        try:
            preco = float(preco)
            if preco <= 0 :
                print('O preço tem que ser maior que 0.')
            else:
                valida_preco = True
        except:
            print("Formato de preço inválido. Use apenas números e separe os centavos por ponto '.'")


    fatura.append([produto,preco])
    total += preco
    valida_preco = False
    repetir = input('Deseja comprar mais algum produdo? s/n  ').lower()

for i in fatura:
    print(i[0], ': ', i[1])
print('O total da fatura é: ' , total)
