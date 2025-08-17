# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado.

# No final, mostre a matriz na tela, com a formatação correta.

lista = []

for l in range(0,3):
    for c in range(0,3):
        num = int(input(f"Digite o valor para a posição {l},{c}: "))
        lista.append(num)
x = 0        
while x < 9:
    print(f"[ {lista[x]} ]", end="")
    if x == 2 or x == 5:
        print()
    x += 1
    