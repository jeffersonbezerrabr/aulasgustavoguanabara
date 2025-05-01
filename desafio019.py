#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles
#e escrevendo o nome do escolhido.

from random import choice

L =[]
x = 0

while x < 4:
    L.append(input("Digite o nome do aluno: "))
    x += 1
    
print(f"O aluno escolhido foi {choice(L)}")

