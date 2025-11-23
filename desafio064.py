#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos
#números foram digitados e qual foi a soma entre eles
#(desconsiderando o flag).

x = 0
soma = 0
while True:
    num = int(input("Digite um número inteiro(999 para sair): "))
    if num != 999:
        x += 1
        soma += num
    if num == 999:
        break
    
print(f"A quantidade de números digitados foi {x}")
print(f"A soma dos números foram {soma}")
        