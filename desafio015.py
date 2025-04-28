#Escreva um programa que pergunte a quantidade de Km percorridos
#por um carro alugado e a quantidade de dias oelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$ 60 por dia e R$ 0,15 por Km rodado.

Dcarro = 60
vdia = 0.15

dias = int(input("Quantos dias ficou com o carro? "))
km = float(input("Quantos Km rodou com o carro? "))

conta = (dias * Dcarro) + (km * vdia)

print(f"O total a pagar é R$ {conta:.2f} ")
