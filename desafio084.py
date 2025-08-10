# Faça um programa que leia nome e peso de várias pessoas,
# Guardando tudo em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
maior = menor = x = 0
while True:
    nome = str(input("Nome: ").strip())
    peso = float(input("Peso: ").strip())
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    if x == 0:
        maior = menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    x += 1
    sair = input("Quer continuar? [S/N]").lower().strip()
    if sair == "n":
        break
    elif sair != "s":
        print("Pessoa cadastrada...")
        print("Digite S para continuar ou N para sair, quando for solicitado.\n")
        continue

print(f"Você cadastrou {x} pessoas")

for c in pessoas:
    if c[1] == maior:
        print(f"O maior peso foi de {c[0]}, pesando {c[1]:.2f} Kg")
    if c[1] == menor:
        print(f"O menor peso foi de {c[0]}, pesando {c[1]:.2f} Kg")

        
