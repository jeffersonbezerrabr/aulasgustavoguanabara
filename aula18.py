# teste = list()
# teste.append("Gustavo")
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = "Maria"
# teste[1] = "22"
# galera.append(teste[:])
# teste[0] = "Luiz"
# teste[1] = 11
# galera.append(teste[:])
# print(teste)
# print(galera)

# galera = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# for i in galera:
#     print(f"O nome da pessoa é {i[0]} e a idade é {i[1]}")

galera = []
dado = []
maior = menor = 0
for c in range(4):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
    
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.\n")
        maior += 1
    else:
        print(f"{p[0]} é menor de idade.\n")
        menor += 1
print(f"Temos {maior} maiores e {menor} menores de idade.")
