#Faça um programa que leia um número inteiro e diga
#se ele é ou não um número primo.

num = int(input("Digite um número inteiro: "))

# Um número primo deve ser maior que 1
if num > 1:
    # Verificar divisores de 2 até a raiz quadrada do número
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
