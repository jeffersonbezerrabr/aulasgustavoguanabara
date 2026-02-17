# Crie a classe Livro, que vai simular a passagem de páginas de um livro,
# considerando também se o usuário chegou ao fim da leitura.

pag = 1
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        
        print(f"Você acabou de abrir o livro '{self.titulo}' que tem {self.paginas} páginas no total. Você está na página {pag}")

        
    def avancar_paginas(self, pagina):
        self.pagina = pagina
        x = 1
        global pag
        while True:
            x += 1
            pag += 1
            print(f"Pág{pag} > ",end="")
            
            if x > self.pagina:
                print(f"Você avançou {self.pagina} páginas e agora está na página {pag}")
                break

            elif pag == self.paginas:
                print(f"Você chegou na pagina {pag}. Essa é a ultima página do livro {self.titulo}")
                break
            
                   
l1 = Livro("Peba", 35)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)