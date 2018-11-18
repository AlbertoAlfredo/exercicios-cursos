from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print("O computador escolheu {}".format(itens[computador]))
print("""
+++++++++++++++++++++++
0 => Pedra
1 => Papel
2 => Tesoura
+++++++++++++++++++++++
""")
pessoa = int(input("Escolha sua jogada: "))
sleep(1)
print("Jo")
sleep(2)
print("ken")
sleep(2)
print("Poh")
sleep(2)
print("O computador escolheu {}".format(itens[computador]))

if computador == 0:
    if pessoa == 0:
        print("Você escolheu {}".format(itens[0]))
        print("Vocês empataram.")
    elif pessoa == 1:
        print("Você escolheu {}".format(itens[1]))
        print("O computador venceu.")
    elif pessoa == 2:
        print("Você escolheu {}".format(itens[2]))
        print("Você venceu!")
    else:
        print("Opção inválida")
elif computador == 1:
    if pessoa == 0:
        print("Você escolheu {}".format(itens[0]))
        print("O computador venceu!")
    elif pessoa == 1:
        print("Você escolheu {}".format(itens[1]))
        print("Vocês empataram.")
    elif pessoa == 2:
        print("Você escolheu {}".format(itens[2]))
        print("Você venceu!")
    else:
        print("Opção inválida")
elif computador == 2:
    if pessoa == 0:
        print("Você escolheu {}".format(itens[0]))
        print("Você perdeu!")
    elif pessoa == 1:
        print("Você escolheu {}".format(itens[1]))
        print("Você venceu!")
    elif pessoa == 2:
        print("Você escolheu {}".format(itens[2]))
        print("Vocês empataram")
    else:
        print("Opção inválida")