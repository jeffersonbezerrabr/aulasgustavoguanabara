#Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento.

#Para salários acima de R$ 1250,00, calcule um aumento de 10%

#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o valor do seu salário: "))

if salario > 1250:
    print(f"O aumento será de 10%, seu novo salário é R${salario + (salario *0.10):.2f}")
else:
    print(f"O aumento será de 15% seu novo salário é R${salario + (salario * 0.15):.2f}")