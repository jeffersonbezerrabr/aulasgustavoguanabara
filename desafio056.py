#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:

# > A média de idade do grupo
# > Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.

maior = 0
homem = ''
x = 0
soma_idade = 0

for c in range(1, 5):
    nome = input(f"Qual o nome da {c}ª pessoa: ").strip()
    idade = int(input(f"Qual a idade da {c}ª pessoa: "))
    sexo = input(f"Qual o sexo da {c} pessoa: ").upper()
    soma_idade += idade
    if c == 1 and sexo == "M":
        maior = idade
        homem = nome
    if sexo =="M" and idade > maior:
        maior = idade
        homem = nome
    if idade < 20 and sexo == "F":
        x += 1
media_idade = soma_idade / c
print(f"A média da idade é {float(media_idade):.2f}")
print(f"O homem mais velho é o {homem}, com {maior} anos")
print(f"{x} mulher(s) tem menos de 20 anos")