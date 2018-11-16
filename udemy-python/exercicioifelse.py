nome = input("Digite o nome do aluno: ")
notap1 = float(input("Digite a nota da primeira prova: "))
notap2 = float(input("Digite a nota da segunda prova: "))
presenca = int(input("Digite o total de presenças em aula: "))
qtd_aulas = 20
media = (notap1 + notap2)/2
assiduidade = float((presenca * 100)/qtd_aulas)

if assiduidade >= 70.0:
    if media >= 6.0:
        print (nome + " você foi aprovado")
    else:
        print(nome + " você foi reprovado por ter média " + str(media))
else:
    print(nome + " você foi reprovado por ter o percentual de assiduidade de " + str(assiduidade) + "%")

