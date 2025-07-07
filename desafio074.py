# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.

# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

from random import sample

numeros = tuple(sample(range(101), 5))
menor = maior = x = y = 0

while x < len(numeros):
    for n in numeros:
        if y == 0:
            menor = maior = n
            y += 1
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
        x += 1
        
print(f"Os números gerados foram: {numeros}")
print(f"O menor número é {menor}")
print(f"O maior número é {maior}")