#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$ 0,45 para viagens mais longas.

distancia = int(input("Qual a distância da sua viagem: "))

ate_200 = 0.50
acima_200 = 0.45

if distancia <= 200:
    valor = distancia * ate_200
    
else:
    valor = distancia * acima_200
    
print(f"O valor a pagar pela sua viagem é de R${float(valor):.2f}")
    