#Desafio 022 - Aula 09

#Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas

#O nome com todas as letras minúsculas.

#Quantas letras ao todo(sem considerar espaços)

#Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()

print(f"O nome com todas as letras maiúsculas: {nome.upper()}")

print(f"\nO nome com todas as letras minúsculas: {nome.lower()}")

nome_sem_espaco = nome.replace(" ", "")
print("\nQuantas letras ao todo(sem considerar os espaços):")
print(len(nome_sem_espaco))

print("\nQuantas letras tem o primeiro nome: ")
if len(nome) > 0:
    primeiro_nome = nome.split()[0]
    print(len(primeiro_nome))
else:
    print("Nenhum nome foi digitado!")