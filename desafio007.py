#Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre sua média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Nota precisa ser entre 0 e 10")
    
else:
    media = (nota1 + nota2) / 2
    print(f"A média é {media:.1f}")
    
if media >= 7:
    print("Aprovado!")
    
elif media >= 5:
    print("Recuperação")

else:
    print("Reprovado")