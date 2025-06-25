#Faça um programa que leia um número qualquer e mostre o seu fatorial.

fatorial = 1
num = int(input("Digite um número: "))
for c in range (1, num+1):
    fatorial *= c

print(f"O fatorial de {num} é {fatorial}")