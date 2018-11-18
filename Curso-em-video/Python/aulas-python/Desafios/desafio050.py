n = 0
for c in range (0, 6):
    n2 = int(input("Digite um valor: "))
    if n2 % 2 == 0:
        n += n2
print("A soma dos número pares é: {}".format(n))