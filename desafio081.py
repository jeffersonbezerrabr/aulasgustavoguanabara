# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    num = input("Digite um número ou [s] para sair: ").lower().strip()
    if num == "s":
        break
    try:
        num_int = int(num)
        lista.append(num_int)
    except ValueError:
        print("Você deve digitar um número\n")
    
print(f"Você digitou {len(lista)} números")
print(f"Segue os valores em ordem decrescente: {sorted(lista)[::-1]}")
if 5 in lista:
    print(f"O número 5 está na lista na posição {lista.index(5)}")
else:
    print("O número 5 não foi digitado.")
    