idade = int(input('Digite sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower().strip(' ')

if idade >= 18:
    if sexo == "m":
        print("Você é homem maior de idade")
    elif sexo == "f":
        print("Você è mulher maior de idade")
    else:
        print("Você digitou a opção de sexo errada")
elif idade < 18:
    if sexo == "m":
        print("Você é garoto menor de idade")
    elif sexo == "f":
        print("Você é garota menor de idade")
    else:
        print("Você digitou a opção errada de sexo")
