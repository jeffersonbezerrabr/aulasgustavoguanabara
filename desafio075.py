# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


tupla_numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

print(f"O valor 9 apareceu {tupla_numeros.count(9)} vezes.")

if 3 in tupla_numeros:
    print(f"O primeiro valor 3 foi digitado na {tupla_numeros.index(3) +1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
    
print(f"Os números pares são ", end="")
for n in tupla_numeros:
    if n % 2 == 0:
        print(n, end=" ")