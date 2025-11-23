#Desafio 024 - Aula 09

#Crie um programa que leia o nome de uma cidade e diga
#se ela começa ou não com nome "SANTO".

cidade = str(input("Digite o nome de uma cidade: ")).strip()

if cidade.lower().startswith("santo"):
    print(f"A cidade {cidade} começa com Santo")
    
else:
    print(f"A cidade {cidade} não começa com Santo")