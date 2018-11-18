# coding: utf-8
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2
print("Com as notas {:.1f} e {:.1f}, a média é {:.1f} ".format(n1, n2, media))
if media < 5:
    print("Você foi reprovado.")
elif media < 7:
    print("Você está de recuperação.")
else:
    print("Você foi aprovado.")