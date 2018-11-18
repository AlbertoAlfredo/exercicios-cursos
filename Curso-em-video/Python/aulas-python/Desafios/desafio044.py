print("Sistema lojas lojadas")
print("""Escolha a opção:
[1] Dinheiro/Cheque (à vista)
[2] Cartão""")
opcao = int(input("Opção: "))
valor = float(input("Digite o valor da compra: "))
if opcao == 1 :
    print("Deconto de 10%, valor final: R$:{:.2f}".format(valor * 0.9))
elif opcao == 2 :
    nparcela = int(input("Digite a quantidade de parcelas: (digite 1 para pagamento à vista) "))
    if nparcela == 1 :
        print("Desconto de 5%, valor final: R$:{:.2f}".format(valor * 0.95))
    elif nparcela == 2 :
        print("Não há desconto, valor final: R$:{:.2f}".format(valor))
    elif nparcela > 2:
        print("Juros de 20%, valor final: R$:{:.2f}".format(valor * 1.2))
    else:
        print("Não há a opção de 0 de parcelas.")
else:
    print("Opção inválida.")