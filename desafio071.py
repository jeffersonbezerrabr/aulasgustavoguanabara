# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuário qual será 
# o valor a ser sacado(número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.

# OBS: Considere que o caixa possui cédulas de:
# R$ 50, R$ 20, R$ 10 e R$ 1.



valor = int(input("Quanto deseja sacar? "))
cont_cedulas = 0
cedula = 50
apagar = valor
while True:
    if apagar >= cedula:
        apagar -= cedula
        cont_cedulas += 1
    else:
        if cont_cedulas > 0:
            print(f"Total de {cont_cedulas} cédulas de R$ {cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont_cedulas = 0
        if apagar == 0:
            break
        