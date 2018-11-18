from math import sin, cos, tan, radians
a = float(input("Digite o ângulo: "))
a = radians(a)
print("""O valor do seno é: {:.2f}
O valor do cosseno é {:.2f}
O valor da tangente é {:.2f}""".format(sin(a), cos(a), tan(a)))