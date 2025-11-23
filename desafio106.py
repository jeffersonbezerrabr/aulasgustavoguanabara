# Exercício Python 106: Faça um mini-sistema que utilize 
# o Interactive Help do Python. O usuário vai digitar o comando 
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', 
# o programa se encerrará. Importante: use cores.

def ajuda(txt):
    texto = f"Acessando o manual do comando {txt}"
    print("~" * len(texto))
    print(texto)
    print("~" * len(texto))
    return help(txt)
    

print("SISTEMA DE AJUDA PyHELP")
print()
comando = ''
while True:
    comando = input("Função ou biblioteca > ")
    if comando.upper() == "FIM":
        print("Até logo")
        break
    else:
        ajuda(comando)


