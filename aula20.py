# Aula funções - Parte 1

# https://www.youtube.com/watch?v=ezfr9d7wd_k&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=29&t=165s

# def soma(a,b):
#     print(f"A = {a} e B = {b}")
#     s = a + b
#     print(f"A soma A + B = {s}")


# soma(4, 5)
# soma(8, 9)
# soma(2, 1)

# def contador(*num):
#     tam = len(num)
#     print(f"Recebi os valores {num} e são ao todo {tam} números.")
    
    
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

