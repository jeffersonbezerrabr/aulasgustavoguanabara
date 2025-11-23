#Crie um programa que leia dois valores e mostre um menu na tela:

num1 = int(input("Digite um número: "))
num2 = int(input("\nDigite mais um número: "))

while True:
    print('''
-----MENU-----
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    print()
    menu = int(input("Escolha uma das opções: "))
    if menu == 5:
        print("\nObrigado. Até mais ...")
        break
    elif menu == 1:
        somar = num1 + num2
        print(f"\nA soma de {num1} + {num2} é {somar}")
    elif menu == 2:
        mult = num1 * num2
        print(f"\nA multiplicação de {num1} x {num2} é {mult}")
    elif menu == 3:
        if num1 > num2:
            print(f"\n{num1} é maior")
        else:
            print(f"\n{num2} é maior")
    elif menu == 4:
        num1 = int(input("\nDigite um número: "))
        num2 = int(input("\nDigite mais um número: "))
    else:
        print("\nOpção invalida. as opções são de 1 a 5.")
        