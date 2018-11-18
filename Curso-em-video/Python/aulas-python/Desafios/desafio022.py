n = str(input("Digite seu nome completo: ")).strip()

print("""Maiuscula: {}
Minuscula: {}
Total de letras: {}
Total de letras no primeiro nome: {}""".format(n.upper(), n.lower(),len(n)-n.count(' '), n.find(' ') ))
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))