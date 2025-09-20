# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre
# uma mensagem com tamanho adaptável.

# Ex:
# escreva("Olá, Mundo!")

#Saida:

# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~

def escreva(msg):
    print("-" * len(msg))
    print(msg)
    print("-" * len(msg))


escreva("Olá, Mundo!")