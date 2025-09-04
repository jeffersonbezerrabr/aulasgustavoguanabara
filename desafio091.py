# Crie um programa onde 4 jogadores joguem um dado e 
# tenham resultados aleatórios. Guarde esses resultados
# em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = {}
x = 1
print("Valores sorteados:\n")
sleep(1)
for j in range(1,5):
    jogadores[f"jogador{j}"] = randint(1,6)
    sleep(1)
    print(f"O jogador {j} tirou ({jogadores[f"jogador{j}"]})")
    
jogadores_ordenado = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

sleep(1)
print("Ranking dos jogadores:\n")
for v in jogadores_ordenado:
        sleep(1)
        print(f"{x}º lugar: {v[0]} com ({v[1]})")
        x += 1
        