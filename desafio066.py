# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

i = 0
soma = 0
while True:
    num = input("Digite um valor (999 para parar): ")
    
    num_int = 0
    num_valido = None
    
    try:
        num_int = int(num)
        num_valido = True
    except:
        num_valido = None
    if num_int == 999:
        break
    
    if num_valido is None:
        print("Digite um número inteiro.")
        continue
    
    soma += num_int
    i += 1
    
print(f"Você digitou {i} numeros e a soma deles foi {soma}")