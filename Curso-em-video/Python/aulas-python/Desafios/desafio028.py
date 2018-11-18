from random import randrange
n = randrange(6)
print("Tente adivinhar qual número entre 0 e 5 foi sorteado ")
chute = int(input("Digite seu chute: "))
if n == chute:
    print("Parabéns você acertou!!!!!!")
else:
    print("Você errou. Mais sorte na próxima.")
print("O número sorteado foi {}".format(n))