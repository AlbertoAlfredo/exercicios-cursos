# -*- coding: utf-8 -*-
nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2018 - nascimento
if idade < 18:
    print ("Você que nasceu em {}, sua idade é {}".format(nascimento, idade))
    print ("Você deve alistar em {}".format(nascimento + 18))
elif idade == 18:
    print ("Você deve se alistar nesse ano.")
else:
    print ("Você deve ter se alistado em {}, se não se alistou deve ir a junta pagar multa.".format(nascimento + 18))