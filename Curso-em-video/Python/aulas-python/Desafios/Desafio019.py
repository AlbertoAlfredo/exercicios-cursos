from random import choice
a1 = input("Digite um nome: ")
a2 = input("Digite outro nome: ")
a3 = input("Digite outro nome: ")
print("O nome sorteado foi: {}".format(choice([a1, a2, a3])))