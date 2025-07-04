
#Tuplas são IMUTÁVEIS

# lanche = ("Hanbúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")

# print(lanche[1])
# print(lanche[:2])
# print(lanche[2:])
# print(lanche[0:2])
# print(lanche[-2])
# print(lanche[-3:])

# for c in lanche:
#     print(f"Eu vou comer {c}")
# print("Comi pra caramba!")

# for co in range(len(lanche)):
#     print(f"{co} - {lanche[co]}")
    
# for pos, comida in enumerate(lanche):
#     print(f"{pos} - {comida}")

# print(sorted(lanche)) # Coloca em ordem

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# d = b + a
# print(c)
# print(d)
# print(len(c))
# print(c.count(5)) # Conta quantas vezes o argumento aparece.
# print(c.index(4)) # verifica o indice do valor informado.
# print(d.index(5, 1)) # o indice de 5 a partir do indice 1

pessoa = ("Jeff", 37, "M", 81.5)
print(f"Nome: {pessoa[0]}")
print(f"Idade: {pessoa[1]}")
print(f"Sexo: {pessoa[2]}")
print(f"Peso: {pessoa[3]}")