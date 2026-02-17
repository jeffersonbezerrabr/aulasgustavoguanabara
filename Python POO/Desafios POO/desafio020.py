# Crie uma classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie também um método que permita mostrar a ficha desse gamer.

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.games = []
        
    def add_favoritos(self, game):
        self.games.append(game)
        
        
    def ficha(self):
        print(f"Jogador: {self.nick}")
        print(f"Nome real: {self.nome}")
        print(f"Jogos favoritos:\n")
        for c in sorted(self.games):
            print(f"- {c}")
        
        
j1 = Gamer("Jefferson", "DeathFox")
j1.add_favoritos("Mario")
j1.add_favoritos("Pokemon")
j1.add_favoritos("Nier Automata")
j1.add_favoritos("Final Fantasy")

j1.ficha()
