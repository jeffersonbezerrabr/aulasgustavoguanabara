# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.

x = menor = total = 0
y = 0
barato = ''
while True:
    produto = input("Qual produto deseja comprar: ").strip()
    valor = float(input("Qual o valor: "))
    total += valor
    y += 1
    if valor > 1000:
        x += 1
    if y == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    sair = input("Deseja continuar [S/N]? ").strip().lower()
    if sair == "n":
        break
print(f"O total gasto foi RS {total}")
print(f"{x} produtos custaram mais de R$ 1000")
print(f"O produto mais barato é {barato}, custando R$ {menor}")