#Desafio 027 - Aula 09

#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

#Exemplo: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = str(input("Digite seu nome completo: ")).strip()

dividido = nome.split()

print(f"Primeiro nome: {dividido[0]}")
print(f"Ultimo nome: {dividido[-1]}")