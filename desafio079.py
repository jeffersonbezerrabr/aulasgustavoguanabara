# Crie um programa onde o usuário possa digitar
# vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro,
# ele não será adicionado.
# No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.

lista = []

while True:
    num = (input("Digite um número ou [s] para sair:  ")).lower().strip()
    if num == "s":
        break
    try:
        int_num = int(num)
        if int_num in lista:
            print("Valor duplicado! Não vou adicionar...")
        else:
            print("Valor adicionado com sucesso...")
            lista.append(int_num)

    except ValueError:
        print("Você precisa digitar um número ou [s] para sair.\n")
    
print(f"\nVocê digitou os seguintes valores: {sorted(lista)}")
