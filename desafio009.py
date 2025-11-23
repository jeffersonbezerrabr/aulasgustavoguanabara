#Faça um programa que leia um número inteiro qualquer
#e mostre na tela sua tabuada.

n = int(input("Digite um número para ver sua tabuada de multiplicação: "))
x = 1
while x < 11:
    print(f"{n} x {x} = {n * x}")
    x += 1