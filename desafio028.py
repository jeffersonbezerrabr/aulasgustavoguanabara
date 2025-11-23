#Escreva um programa que faça o computador "Pensar"
#em um número inteiro entre 0 e 5 e peça para o 
#usuário tentar descobrir qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

numero_aleatorio = randint(0,5)

while True:
    print("Tente acertar o número que o computador gerou.")
    numero = int(input("Chute um número de 0 a 5: "))
    if numero == numero_aleatorio:
        print(f"Parabéns você acertou")
        break
    elif numero < numero_aleatorio:
        print("Precisa chutar um número maior!")
    else:
        print("Precisa chutar um número menor")