#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
#em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.

from random import randint
numero_PC = randint(0, 10)
x = 0
while True:
    chute = int(input("Chute um número: "))
    if chute == numero_PC:
        x += 1
        print(f"Parabéns, vocẽ acertou em {x} tentativas.")
        break
    elif chute < numero_PC:
        print("Você precisa chutar mais alto.")
        x += 1
    else:
        print("Você precisa chutar mais baixo.")
        x += 1
        