# Crie uma tupla preenchida com os 20 primeiros colocados
# da tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os ultimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Fortaleza.

times = ("Flamengo", "Cruzeiro", "Bragantino", "Palmeiras", "Fluminense", 
         "Botafogo", "Bahia", "Mirassol", "Atlético-MG", "Ceará",
         "Corinthians", "Gremio", "São Paulo", "Internacional", 
         "Vasco da Gama", "Vitória", "Fortaleza", "Santos", 
         "Juventude", "Sport")
print("=" * 50)
print(f"Os 5 primeiros colocados são: {times[:5]}")
print("=" * 50)
print(f"Os 4 ultimos colocados são: {times[-4:]}")
print("=" * 50)
print(f"Times em ordem alfabética: {sorted(times)}")
print("=" * 50)
for p, time in enumerate(times):
    if time == "Fortaleza":
        print(f"Fortaleza está na {p+1}ª posição.")
        
