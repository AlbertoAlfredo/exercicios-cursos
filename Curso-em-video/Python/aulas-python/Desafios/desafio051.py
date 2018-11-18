v = int(input("Digite o valor inicial da progreção: "))
co = int(input("Digite o valor da constante: "))
n = int(input("Digite o número de elementos: "))
s = 0

for c in range(v , n, co):
    if s < 10:
        print(c)
        s +=1