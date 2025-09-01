# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))
situacao = ''

if aluno["media"] < 6:
    situacao = "Reprovado"
elif aluno["media"] <= 6.9:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"
    
print(f"Nome é igual a {aluno['nome']}")
print(f"Média é igual a {aluno['media']}")
print(f"Situação é igual a {situacao}")
