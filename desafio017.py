#Faça um programa que leia o comprimento
#do cateto oposto e do cateto adjacente
#de um triângulo retângulo, calcule e 
#mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjascente = float(input("Digite o valor do cateto adjascente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjascente)

print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")