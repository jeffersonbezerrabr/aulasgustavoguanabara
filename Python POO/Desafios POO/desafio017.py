# Crie a classe Produto, onde podemos cadastrar nome e o preço.
# Crie também um método que mostre uma etiqueta de preço do produto.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def etiqueta(self):
        largura = 20
        print(f"{self.nome: ^{largura}}")
        print(f"{'':-^{largura}}")
        print(f"R${self.preco:.^{largura}.2f}")
        print()
        
p1 = Produto("PC Gamer", 2500)
p2 = Produto("Notebook Gamer", 8000)

p1.etiqueta()
p2.etiqueta()
