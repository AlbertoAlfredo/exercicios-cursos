print("\033[7;30m-="*20, "\033[m")
print("\033[1;33;44mANALISADOR DE TRIÂNGULO\033[m")
print("\033[7;30m=-"*20, "\033[m")
l1 = float(input("Digite o primeiro segmento: "))
l2 = float(input("Digite o segundo segmento: "))
l3 = float(input("Digite o terceiro segmento: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Esses segmentos formam um triângulo")
else:
    print("Esses segmentos não formam um triângulo")