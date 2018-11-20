nome = input("Digite o nome do aluno: ")
qtd_aulas = 20
def verifica_nota():
    erro = True
    while erro:
        nota = input("Digite a nota da prova: ")
        try:
            nota = float(nota)
            if nota < 0 or nota > 10:
                print("A nota deve ser maior que 0 e menor ou igual a 10")
            else:
                erro = False
        except:
            print("Formato inválido, digite a nota entre 0 e 10 e separe o decimal por ponto '.': ")
    return nota

print("\nPrimeira prova")
notap1 = verifica_nota()
print("\nSegunda prova")
notap2 = verifica_nota()

erro_presenca = True
while erro_presenca:
    presenca = input("Digite o total de presenças em aula: ")
    try:
        presenca = int(presenca)
        if presenca < 0 or presenca > 20:
            print("A presença deve ser um valor maior que 0 e menor ou igual a 20. ")
        erro_presenca = False
    except:
        print("Formato inválido, a presença deve ser número inteiro.")

media = (notap1 + notap2)/2
assiduidade = float((presenca * 100)/qtd_aulas)

if assiduidade >= 70.0:
    if media >= 6.0:
        print (nome + " você foi aprovado")
    else:
        print(nome + " você foi reprovado por ter média " + str(media))
else:
    print(nome + " você foi reprovado por ter o percentual de assiduidade de " + str(assiduidade) + "%")

