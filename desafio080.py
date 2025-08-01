# Crie um programa onde o usuário possa digitar cinco
# valores númericos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort())

# No final, mostre a lista ordenada na tela.

lista = []

for c in range(5):
    num = input("Digite um valor: ").strip()
    try:
        int_num = int(num)
        if c == 0 or int_num > lista[-1]:
            lista.append(int_num)
            print("Adicionado ao final da lista...")  
        else:
            pos = 0
            while pos < len(lista):
                if int_num <= lista[pos]:
                    lista.insert(pos, int_num)
                    print(f"Adicionado na posição {pos} da lista")
                    break
                pos += 1
    except ValueError:
        print("Digite um valor inteiro.")

print("=" * 40)
print(f"Os valores digitados em ordem foram: {lista}")
