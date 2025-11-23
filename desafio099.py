# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores
# e dizer qual deles é o maior.

from time import sleep

def maior(*args):
    cont = maior = 0
    print("-=" * 30)
    print("Anaisando os valores informados...")
    for n in args:
        print(f"{n} ", end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f"foram informados {cont} ao todo.")
    print(f"O maior valor informado foi {maior}")
    print("-=" * 30)
    
maior(2,9,4,5,7,1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()
