#Crie um algoritimo que leia um número ee mostre o seu dobro,
#seu triplo e raiz quadrara

numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print(f"O dobro de {numero} é {dobro}")
print(f"O triplo de {numero} é {triplo}")
print(f"A raiz de {numero} é {raiz:2f}")
