#  DOCSTRING

# def contador(i, f, p ):
#     """
#     Faz uma contagem e mostra na tela

#     Args:
#         i (parametro): Início da contagem
#         f (parametro): Fim da contagem
#         p (parametro): Passo da contagem"""
#     c = i
#     while i <= f:
#         print(f"{c} ", end='')
#         c += p
#     print("FIM!")
    
# help(contador)

# ARGUMENTOS POSICIONAIS

# def somar(a=0, b=0, c=0):
    
#     s = a + b + c
#     print(f"A soma vale {s}")
    
# somar(1, 2, 3)
# somar(1, 2)


# ESCOPO DE VARIAVEIS

# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f"A dentro vale {a}")
#     print(f"B dentro vale {b}")
#     print(f"C dentro vale {c}")


# a = 5
# teste(a)
# print(f"A fora vale {a}")
# #print(f"B dentro vale {b}") # Não funciona pois b só existe no escopo local
# #print(f"C dentro vale {c}") # Não funciona pois c só existe no escopo local


# RETORNANDO VALORES

# def somar(a=0, b=0, c=0):
    
#     s = a + b + c
#     return s
    
# r1 = somar(1, 2, 3)
# r2 = somar(1, 2)
# r3 = somar(4)

# print(f"Meus cálculos deram {r1}, {r2}, {r3}")
