num = int(input('Digite um número inteiro: '))
print("""Escolha a base para conversão:
[1] binário
[2] octal
[3] hexadecimal""")
opcao = int(input("Digite a opção: "))
if opcao == 1:
    print("A converção em binário de {} é {}.".format(num, bin(num)[2:]))
elif opcao == 2:
    print("A conversão em octal de {} é {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("A conversão em hexadecimal de {} é {}".format(num, hex(num)[2:]))
else:
    print("Opção não encontrada.")