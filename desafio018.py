#Faça um programa que leia um ângulo qualquer e mostre
#na tela o valor do seno, cosseno e tangente desse ângulo.

import math

graus = int(input("Digite um ângulo: "))

radianos = math.radians(graus)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"O seno de {graus}º é {seno:.2f}")
print(f"O cosseno de {graus}º é {cosseno:.2f}")
print(f"A Tangente de {graus}º é {tangente:.2f}")