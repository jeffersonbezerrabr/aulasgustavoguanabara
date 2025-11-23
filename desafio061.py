#Desenvolva um programa que leia o primeiro termo
#e a razão de uma PA. No final, mostre os 
#10 primeiros termos dessa progressão.

x = 0
termo = int(input("Termo: "))
razao = int(input("Razão: "))
while x < 10:
    print(f"{termo} > ", end='')
    termo += razao
    x += 1
print("FIM")
