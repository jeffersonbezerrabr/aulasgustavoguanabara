#Crie um programa que leia duas notas de um aluno e calcule
#sua média, mostrando uma mensagem no final,
#de acordo com a média atingida:

#- Média abaixo de 5.0: Reprovador

#-Média entre 5.0 e 6.9: Recuperação

#- Média 7.0 ou superior: Aprovado

Notas = []
x = 0

while x < 2:
    nota = float(input("Digite sua nota: "))
    Notas.append(nota)
    x += 1
media = (Notas[0] + Notas[1]) / 2

if media < 5:
    print(f"REPROVADO! Sua média foi {media:.2f}.")

elif 5 <= media < 7:
    print(f"RECUPERAÇÃO! Sua média foi {media:.2f}")
    
else:
    print(f"APROVADO! Sua média foi {media:.2f}")