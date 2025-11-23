#faça um algoritimo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento.

salario = float(input("Quanto é o seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento

print(f"Seu salário com aumento de 15% ficou R$ {novo_salario:.2f}")
