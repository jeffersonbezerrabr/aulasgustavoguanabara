# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores impares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

numeros = []
par = []
impar = []
while True:
    num = input("Digite um número inteiro ou [s] para sair: ").lower().strip()
    if num == "s":
        break
    try:
        int_num = int(num)
        numeros.append(int_num)
    except ValueError:
        print("Você precisa digitar um número inteiro ou [s] para sair\n")
        
for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
        
print(f"Lista completa: {numeros}\n")
print(f"Lista com números pares: {par}\n")
print(f"Lista com números impares: {impar}\n")