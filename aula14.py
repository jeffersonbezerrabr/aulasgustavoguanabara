#While

#for c in range(1, 11):
#    print(c)

'''x = 1

while x < 11:
    print(x)
    x += 1'''
    
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
        
print(f"Você digitou {par} numeros pares e {impar} numeros impares")