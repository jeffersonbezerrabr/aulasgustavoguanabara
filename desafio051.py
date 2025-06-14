#Desenvolva um programa que leia o primeiro termo
#e a razão de uma PA. No final, mostre os 
#10 primeiros termos dessa progressão.

PA = []
termo = int(input("Digite o primeiro: "))
razao = int(input("Digite a razão da PA: "))

for c in range(0, 10):
    PA.append(termo)
    termo += razao

print(f"Os 10 primeiros termos da PA são: {PA}")
    

