#O mesmo professor do desafio anterior quer sortear a ordem
#de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.

from random import shuffle

lista_alunos = []
x = 0

while x < 4:
    lista_alunos.append(input("Digite o nome do aluno: "))
    x += 1
shuffle(lista_alunos)
print(f"Segue a ordem da apresentação dos alunos: {lista_alunos}")