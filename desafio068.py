# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo.

from random import randint
i = num_int = 0
while True:
    print("=-" * 15)
    print("Vamos jogar par ou ímpar")
    print("=-" * 15)
    num = input("Digite um valor inteiro: ")
    escolha = input("Par ou ímpar? [P/I]").strip().upper()
    pc = randint(1,10)
    num_valido = None
    
    try:
        num_int = int(num)
        num_valido = True
    except:
        num_valido = None
        
    if num_valido is None:
        print("Digite um número inteiro")
        continue
    
    escolha_valida = "PIÍ"
    
    if escolha not in escolha_valida:
        print("Escolha invalida! Escolha Par ou Ímpar")
        continue
    
    soma = num_int + pc
    resultado = soma % 2
    
    if escolha == "P" and resultado == 1:
        print(f"você jogou {num_int} e o PC {pc}.")
        print(f"O Total foi {soma} e esse valor é ÍMPAR")
        print("Você perdeu!")
        print(f"Você venceu {i} vezes")
        break
    elif escolha == "P" and resultado == 0:
        i += 1
        print(f"você jogou {num_int} e o PC {pc}.")
        print(f"O Total foi {soma} e esse valor é PAR")
        print("Você venceu!")
        print("Vamos jogar novamente...")
        
    elif escolha == "I" and resultado == 1:
        i += 1
        print(f"você jogou {num_int} e o PC {pc}.")
        print(f"O Total foi {soma} e esse valor é ÍMPAR")
        print("Você venceu!")
        print("Vamos jogar novamente...")
        
    elif escolha == "I" and resultado == 0:
        print(f"você jogou {num_int} e o PC {pc}.")
        print(f"O Total foi {soma} e esse valor é PAR")
        print("Você perdeu!")
        print(f"Você venceu {i} vezes")
        break