#Escreva um programa que leia um número n inteiro qualquer
#e mostre na tela os n primeiros elementos de uma
#sequencia de fibonacci.

n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
x = 3
print(f"{t1} > {t2} ", end='')
while x <= n:
    t3 = t1 + t2
    print(f"> {t3} ", end='')
    t1 = t2
    t2 = t3
    x += 1
print("> FIM")