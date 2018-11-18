import math
c1 = float(input('Digite o tamanho do cateto '))
c2 = float(input('Digite o tamanho do outro cateto '))
h = math.hypot(c1,c2)
print("O valor da hipotenusa é {:.2f}".format(h))