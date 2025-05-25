#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base da conversão:

#1 para binário
#2 para octal
#3 para hexadecimal

numero = int(input("Digite um número inteiro: "))
print("="*30)
conversao = int(input("""
1 - Converter para binário
2 - Converter para octal
3 - Converter para hexadecimal
\n"""))
print("="*30)
if conversao == 1:
    binario = bin(numero)
    print(f"{numero} em binário é {binario[2:]}")
    
elif conversao == 2:
    octal = oct(numero)
    print(f"{numero} em octal é {octal[2:]}")
    
elif conversao == 3:
    hexa = hex(numero)
    print(f"{numero} em hexadecimal é {hexa[2:]}")
    
else:
    print("Opção invalda. Tente novamente!")