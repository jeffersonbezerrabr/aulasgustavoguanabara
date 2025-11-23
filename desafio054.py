#Crie um programa que leia o ano de nascimento de sete pssoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.

from datetime import date
x = 0
y = 0
ano_atual = date.today().year
for c in range(1, 8):
    ano = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    if ano_atual - ano >= 21:
        x += 1
    else:
        y += 1
print(f"{x} pessoas são maiores de idade")
print()
print(f"{y} pessoas são menores de idade.")