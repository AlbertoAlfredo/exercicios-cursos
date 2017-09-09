s = float(input("Digite seu salário: "))
if s > 1250:
    aumento = 0.10
else:
    aumento = 0.15
aumentoReais = s * aumento
print("Seu aumento foi de {}%, que equivale a R$:{:.2f} e com isso seu salário será de R$:{:.2f}.".format(aumento * 100, aumentoReais, s + aumentoReais))