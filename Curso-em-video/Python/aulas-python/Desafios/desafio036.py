# coding = utf8
valorEmprestimo = float(input("Digite o valor requistado para o emprastimo: "))
valorSalario = float(input("Digite o valor do salario: "))
tempo = int(input("Digite em quantos anos de prestacoes o cliente deseja: "))
valorParcela = valorEmprestimo / (tempo * 12)
print(f"O valor do emprestimo pedido e R$:{valorEmprestimo}, o salário do cliente e R$:{valorSalario}.")
print(f"O tempo de pagamento do emprestimo e {tempo} anos e o valor da parcela e R$:{valorParcela}")
if valorParcela <= valorSalario * 0.3:
    print("O emprestimo foi aprovado.")
else:
    print("O emprestimo foi reprovado.")
