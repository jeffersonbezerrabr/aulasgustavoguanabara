# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parametros opcionais: o nome de um
# jogador e quantos gols ele marcou.

# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=None, gols=None):

    if jogador == '' and tot_gols == '':
        return f"O jogador <desconhecido> fez 0 gol(s) no campeonato."
    elif jogador == '':
        return f"O jogador <desconhecido> fez {tot_gols} gol(s) no campeonato."
    else:
        return f"O jogador {jogador} fez {tot_gols} gol(s) no campeonato."
    
    
        
jogador = input("Nome do jogador: ")
tot_gols = input("Número de gols: ")

print(ficha(jogador,tot_gols))