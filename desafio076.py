# Crie um programa que tenha uma tupla única com
# nomes de produtos e seus respectivos preços, na sequência.

# No final, mostre uma lstagem de preços, organizando
# os dados em forma tabular.

listagem = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.90,
            "Estojo", 25, "Transferidor", 4.20, "Compasso", 9.99,
            "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
x = 0
print("-" * 50)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-" * 50)
while x < len(listagem):
    for c in range(1, len(listagem), 2):
        print(f"{listagem[x]:.<30} R$: {float(listagem[c]):.2f}")
        x += 2
print("-" * 50)
