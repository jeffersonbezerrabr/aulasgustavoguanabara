#Faça um programa que leia o ano de nascimento de um jovem
#e informe, de acordo com sua idade:

#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo
#que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input("Que ano você nasceu? "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade < 18:
    print("Você ainda vai se alistar.")
    print(f"Faltam {18 - idade} anos")
    
elif idade == 18:
    print("Está na hora de se alistar!")
    print(f"Você tem {idade} anos")
    
else:
    print("Passou do tempo de se alistar!")
    print(f"Você está {idade - 18} anos atrasado!")