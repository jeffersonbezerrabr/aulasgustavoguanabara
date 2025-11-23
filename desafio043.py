#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input("Qual o seu peso (em Kg)? "))
altura = float(input("Qual sua altura (Exemplo: 1.70)? "))
imc = peso / (altura * altura)  # Usar ** para exponenciação

# Verificação do status de acordo com o IMC
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:  # Correção da condição
    print("Peso ideal")
elif 25 <= imc < 30:  # Correção da condição
    print("Sobrepeso")
elif 30 <= imc < 40:  # Correção da condição
    print("Obesidade")
else:
    print("Obesidade mórbida")

# Imprimir o valor do IMC com duas casas decimais
print(f"IMC: {imc:.2f}")
