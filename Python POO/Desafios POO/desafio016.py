# Crie uma classe funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permite ao funcionário se apresentar.

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentacao(self):
        return(f"Olá, eu sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Jeff Codes")
        
c1 = Funcionario("Jeff", "TI", "Programador")
print(c1.apresentacao())

c2 = Funcionario("Luiz", "TI", "Programador")
print(c2.apresentacao())