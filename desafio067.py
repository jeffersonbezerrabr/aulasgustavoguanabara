# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando 
# o número solicitado for negativo.

while True:
    num = input("Quer ver a tabuada de qual valor? ")
    print("=*" * 20)
    x = 1
    num_int = 0
    num_valido = None
    
    try:
        num_int = int(num)
        num_valido = True
    except:
        num_valido = None
    
    if num_valido is None:
        print("Digite um número inteiro.")
        continue
    
    if num_int < 0:
        print("Encerrando...")
        break
    while x <= 10:
        print(f'{num_int} x {x} = {num_int * x}')
        x += 1
        print("-" * 15)
        if x > 10:
            print("=*" * 20)
    