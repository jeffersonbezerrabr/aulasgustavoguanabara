# Faça um programa que tenha uma lista chamada números e
# duas funções chamadas sorteio() e somaPat().
# A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma
# entre os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = []

def sorteio(lista):
    print(f"Os números sorteados foram: ", end='')
    for c in range(5):
        n = randint(1,99)
        lista.append(n)
        print(f"{n} ", end='', flush=True)
        sleep(0.5)
    


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f"\nA soma dos números pares foi: {soma}")
    


sorteio(numeros)
somaPar(numeros)