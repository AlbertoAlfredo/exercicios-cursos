km = int(input("Digite a quantidade de km rodados: "))
dia = int(input("Digite a quantidade de dias que o cliente ficou com o carro: "))
valorKm = km * 0.15
valorDia = dia * 60
valorTotal = valorDia + valorKm
print("""O valor por km é R$:{:.2f}
O valor pelas diárias é R$:{:.2f}
O valor total a ser pago é R$:{:.2f}""".format(valorKm, valorDia, valorTotal))