#Faça um programa que leia um número qualquer e mostre o seu fatorial.

'''num = int(input("Digite um número: "))
fatorial = 1
x = 1
while x <= num:
    fatorial *= x
    x += 1

print(fatorial)'''

num = int(input("Digite um número: "))
c = num
f = 1
while c > 0:
    print(f"{c}", end = '')
    print(" x " if c > 1 else " = ", end = '')
    f *= c
    c -= 1
print(f"{f}")