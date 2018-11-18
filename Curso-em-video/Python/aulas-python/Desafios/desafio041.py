# coding: utf-8
from datetime import date
ano = date.today().year
nascimento = int(input("Digite o ano de seu nascimento: "))
idade = ano - nascimento
if idade <= 9:
    print("Atleta mirim")
elif idade <= 14:
    print("Atleta infantil")
elif idade <= 19:
    print("Atleta junior")
elif idade <= 25:
    print("Atleta sênior")
else:
    print("Atleta master")
