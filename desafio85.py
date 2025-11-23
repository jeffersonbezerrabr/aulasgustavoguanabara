# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final,
# mostre ps valores pares e impares em ordem crescente.

lista = [[], []]

for c in range(1, 8):
    while True:  # Garante que só sai quando digitar corretamente
        num = input(f"Digite o {c}º valor: ")
        try:
            int_num = int(num)
            if int_num % 2 == 0:
                lista[0].append(int_num)
            else:
                lista[1].append(int_num)
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Digite um número inteiro válido.")

print(f"Os valores pares digitados foram: {sorted(lista[0])}")
print(f"Os valores ímpares digitados foram: {sorted(lista[1])}")

            