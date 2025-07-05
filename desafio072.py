# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.

#Seu programa deverá ler um número pelo teclado
# (entre 0 a 20) e mostrá-lo por extenso.

tupla = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte" )

while True:
    valor = input("Digite um número entre 0 a 20: ")
    int_valor = int(valor)
    if 0 <= int_valor <=20:
        break
print(f"{tupla[int_valor]}")