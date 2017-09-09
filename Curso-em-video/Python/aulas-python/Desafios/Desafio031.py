d = int(input("Digite a distância da viagem em km: "))
if d < 200:
    print("O preço da passagem é: R$:{:.2f}".format(float(d * 0.5)))
else:
    print("O preço da passagem é: R${:.2f}".format(float(d * 0.45)))