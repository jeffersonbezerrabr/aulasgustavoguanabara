for c in range(1, 7):
    print(c)
print("FIM")

print("*-*"*20)

for c in range(6, 0, -1):
    print(c)
print("FIM")
print("*-*"*20)

for c in range(0, 7, 2):
    print(c)
print("FIM")

print("*-*"*20)

n = int(input("Digite um número: "))
for c in range(0, n +1):
    print(c)
print("FIM")

print("*-*"*20)

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
print("fim")

print("*-*"*20)

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n
print("O somatorio dos valores foi", s)

