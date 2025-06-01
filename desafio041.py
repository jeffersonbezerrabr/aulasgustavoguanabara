#A confederação Nacional de Natação precisa de um programa
#que leia o ano de nascimento de um atleta e mostre
#sua categoria, de acordo com a idade:

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: Master

from datetime import date
ano_atual = date.today().year
ano = int(input("Qual o ano que você nasceu? "))
idade = ano_atual - ano

if idade <= 9:
    print(f"Você tem {idade} anos. Sua categoria é MIRIM")
elif idade <= 14:
    print(f"Você tem {idade} anos. Sua categoria é INFANTIL")
elif idade <= 19:
    print(f"VocÊ tem {idade} anos. Sua categoria é JUNIOR")
elif idade == 20:
    print(f"Você tem {idade} anos. Sua categoria é SÊNIOR")
else:
    print(f"Você tem {idade} anos. Sua categoria é MASTER")