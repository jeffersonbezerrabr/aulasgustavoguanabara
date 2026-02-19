# Cria a classe Caneta, que simule o funcionamento de uma caneta colorida,
# podendo escrever frases na cor relativa.

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True
        
    def destampar(self):
        self.tampada = False
        
    def escrever(self, texto):
        if self.tampada == True:
            print(f"A caneta {self.cor} está tampada")
        else:
            self.texto = texto
            if self.cor == "vermelho":
                print(f"\033[31m{texto}\033[m")
            elif self.cor == "azul":
                print(f"\033[34m{texto}\033[m")
            elif self.cor == "verde":
                print(f"\033[32m{texto}\033[m")
    
    def quebrar_linha(self, valor=False):
        self.valor = valor
        if self.valor:
            for c in range(self.valor):
                print()
        else:
            for c in range(1):
                print()
            
              
        
c1 = Caneta("vermelho")
c2 = Caneta("azul")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Desenrolado")
c2.quebrar_linha(2)
c3.escrever("Teste2")