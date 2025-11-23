#Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar
#que tipo de triangulo será formado:

# - Equilátero: Todos os lados são iguais
# - Isósceles: Dois lados iguais
# - Escaleno: todos os lados diferentes

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

# Verificação se as retas podem formar um triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    # Verificação do tipo de triângulo
    if r1 == r2 == r3:
        print("O triângulo é Equilátero.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("O triângulo é Isósceles.")
    else:
        print("O triângulo é Escaleno.")
else:
    print("As medidas fornecidas não formam um triângulo.")
