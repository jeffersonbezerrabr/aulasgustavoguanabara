#Faça um programa que leia três números e mostre,
#qual é o maior e qual é o menor.

L = []
x = 0

while x < 3:
    numero = int(input("Digite um número: "))
    L.append(numero)
    x += 1
    
print(f"O maior número é o: {max(L)}")
print(f"O menor número é o: {min(L)}")
