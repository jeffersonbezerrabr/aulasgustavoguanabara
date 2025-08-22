# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = []
soma = soma_3 = maior =  0
for l in range(0,3):
    for c in range(0,3):
        num = int(input(f"Digite o valor da posição {l},{c}: "))
        lista.append(num)
        
for v in range(0,9):
    print(f"[ {lista[v]} ]", end="")
    if v == 2 or v == 5:
        print()
for v in range(0,9):
    if lista[v] % 2 == 0:
        soma += lista[v]
print()
print(f"\nA soma dos valores pares é: {soma}")

for v in range(2,9,3):
    soma_3 += lista[v]
print(f"\nA soma dos valores da coluna 3 é: {soma_3}") 

for v in range(3,6):
    if v == 3:
        maior = lista[v]
    if lista[v] > maior:
        maior = lista[v]
print(f"\nO maior valor da segunda linha é: {maior}")
