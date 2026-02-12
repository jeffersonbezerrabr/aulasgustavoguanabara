# Crie uma classe Churrasco, onde seja posível informar quantas pessoas
# vão participar e mostre quanto de carne deve ser comprado, 
# o custo total do churrasco e o preço por pessoa.

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
        
    def analisar(self):
        valor_kg = 82.40
        consumo_pessoa = 0.40
        total_kg = self.quantidade * consumo_pessoa
        custo_total = total_kg * valor_kg
        custo_pessoa = custo_total / self.quantidade
        
        print(f"Analisando o {self.titulo} com {self.quantidade} convidados")
        print(f"Cada participante comerá {consumo_pessoa}Kg e cada Kg custa R${valor_kg:.2f}")
        print(f"Recomendo comprar {total_kg:.3f}Kg de carne")
        print(f"O custo total será de R${custo_total:.2f}")
        print(f"Cada pessoa pagará R${custo_pessoa:.2f} para participar")
        
c1 = Churrasco("Churras dos Amigos", 3)
c1.analisar()
