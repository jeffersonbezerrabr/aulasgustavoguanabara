#Escreva um programa que leia um valor em metros
#e o converta para centimetros e milimetros

metro = int(input("Digite um valor em metros para converter em centimetros e milimitros: "))
centimetros = metro * 100
milimetro = metro * 1000

print(f"{metro} metros convertido para centrimetos: {centimetros}")
print(f"{metro} metros convertido para milimetros: {milimetro}")
