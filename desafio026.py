#Desafio 026 - Aula 09

#Faça um programa que leia uma frase pelo telcado e mostre:

#Quantas vezer aparece a letra "A".

#Em que posição ela aparece a primeira vez.

#Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip()
quantidade_a = frase.lower().count("a")

if quantidade_a > 0:
    print(f"A letra (a) aparece {quantidade_a} vezes")
    print(f"A posição da primeira letra (a) é: {frase.lower().find('a')+1}")
    print(f"A posição da ultima letra (a) é: {frase.lower().rfind('a')+1}")
    
else:
    print("A letra 'a' não aparece na frase.")