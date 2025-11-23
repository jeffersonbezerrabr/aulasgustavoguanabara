#Faça um programa que leia o sexo de uma pessoa,
#mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente
#até ter um valor correto.

while True:
    sexo = str(input("Qual o seu sexo(Digite M ou F): ")).upper().strip()[0]
    if sexo not in "MF":
        print("Opção invalida. Digite M ou F")
    else:
        print("Muito obrigado")
        break