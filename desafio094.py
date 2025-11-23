# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos
# os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas.
# b) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

lista = []
dados = {}
cont = soma = media = 0
while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    while True:
        dados["sexo"] = str(input("Sexo: [M/F] ")).upper()[0]
        if dados["sexo"] in "MF":
            break
        print("Erro! Por favor, digite apenas M ou F")
    dados["idade"] = int(input("Idade: "))
    soma += dados["idade"]
    lista.append(dados.copy())
    while True:
        resp = input("Quer continuar? [S/N]").upper()[0]
        if resp in "SN":
            cont += 1
            break
        print("Erro! Responda apenas S ou N.")
    if resp == "N":
        break
 
print("-=" * 30)
print(lista)
print("-=" * 30)

print(f"A) Foram cadastradas {cont} pessoas.")
media = soma / len(lista)
print(f"B) A média de idade é de {media:5.2f} anos.")
print(f"C) As mulheres cadastradas foram, ", end="")
for p in lista:
    if p["sexo"] in "Ff":
        print(f"{p['nome']}, ", end='')
print()
print("D) Lista das pessoas que estão acima da média: ")
for p in lista:
    if p["idade"] >= media:
        print("     ")
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< ENCERRADO >>")
