#Escreva um programa que leia dois números inteiros e compare-os,
#mostrando na tela uma mensagem:

# O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print("O primeiro valor é maior!")
    print(f"{num1} > {num2}")
elif num2 > num1:
    print("O segundo valor é maior!")
    print(f"{num2} > {num1}")
else:
    print("Não existe valor maior, os dois são iguais!")
    print(f"{num1} = {num2}")
    