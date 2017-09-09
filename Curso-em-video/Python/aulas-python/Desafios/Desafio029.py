v = int(input("Digite a velocidade do carro: "))
if v > 80:
    print("Você está acima do limite, sua multa é: R$:{:.2f}".format((v - 80) * 7))
else:
    print("Você está dentro do limite de velocidade, continue assim.")