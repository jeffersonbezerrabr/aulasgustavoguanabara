# Faça um programa que tenha uma função chamada area(),
# que receba as dimensões de um terreno retangular(largura e comprimento)
# e mostre a área do terreno.

def titulo(texto):
    print(texto)
    print("-" * 30)


def area(larg, comp):
    dimensao = larg * comp
    print(f"A área de um terreno {larg} x {comp} é de {dimensao}m².")
  
    
titulo("Controle de terrenos")

l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))

area(l, c)
