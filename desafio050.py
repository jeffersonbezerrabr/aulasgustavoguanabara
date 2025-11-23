#Desenvolva um programa que leia seus números inteiros
#e mostre a soma apenas daqueles que forem pares.
#Se o valor for ímpar, desconsidere-o.

s = 0
x = 0

for c in range(1, 7):
    n = int(input(f"Digite o {c} valor: "))
    if n % 2 == 0:
        s += n
        x += 1
print(f"Você informou {x} números pares e a soma foi {s}")
           
'''L = []

for c in range(0, 6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        L.append(n)     

print(f"A soma dos números pares é {sum(L)}")'''