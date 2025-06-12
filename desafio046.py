#Desafio 046

#Faça um programa que mostre na tela uma contagem regressiva
#para o estouro de fogos de artificio, indo de 10 até 0,
#com uma pausa de 1 segundo entre eles.

from time import sleep
print("Contagem regressiva para os fogos!")
sleep(1)
for c in range(10, -1, -1):
    print(f"{c}...")
    sleep(1)
print("FOGOS....")
    