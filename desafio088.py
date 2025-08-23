# Faça um programa que ajude um jogador da 
# MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import sample
from time import sleep

jogos = []

qntd = int(input("Quantos jogos você quer que eu sorteie? "))

for c in range(qntd):
    jogo = sorted(sample(range(1, 61), 6))
    jogos.append(jogo)

print("-" * 30)
print(f" Sorteando {qntd} Jogos")
print("-" * 30)

for i, jogo in enumerate(jogos):
    print(f"Jogo {i +1}: {jogo}")
    sleep(1)

print("-" * 30)
print("Boa sorte!")
