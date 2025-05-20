#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

Ano = int(input("Que ano quer analisar? Digite 0 para analisar o ano atual:  "))
if Ano == 0:
    Ano = date.today().year
if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
    print(f"{Ano} é um ano bissexto")
    
else:
    print(f"{Ano} não é um ano bissexto")