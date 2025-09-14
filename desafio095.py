# Aprimore o DESAFIO 093 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de 
# detalhes do aproveitamento de cada jogador.
time = []
dados = {}
partidas = []

while True:
    dados.clear()
    dados["nome"] = str(input("Nome do jogador: "))
    jogos = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    partidas.clear()
    for g in range(1, jogos+1):
        partidas.append(int(input(f"Quantos gols na partida {g}? ")))    
    dados["gols"] = partidas[:]
    dados["total"] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N")
    if resp == "N":
        break
print("-" * 40)
print("cod ", end='')
for i in dados.keys():
    print(f"{i:<15}", end='')
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f" {str(d):<15}", end='')
    print()
print("-" * 40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com código {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:")
        for i, g in enumerate(time[busca]["gols"]):
            print(f"   No jogo {i+1} fez {g} gols.")
    print("-" * 40)
print("<< VOLTE SEMPRE >>")
            
