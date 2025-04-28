#faça um programa que leia a largura e a altura
#de uma parede em metros, calcule a sua área e a 
#quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta
#pinta uma área de 2m².

largura = float(input("Qual a largura da parede (em metros): "))
altura = float(input("Qual a altura da parede (em metros): "))

area = altura * largura

tinta = area / 2

print(f"Sua parede tem {area:.2f}m² de área.")
print(f"você precisará de {tinta:.1f} litros de tinta para pintá-la.")