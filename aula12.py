nome = str(input("Qual o seu nome? "))
if nome.lower() == "Gustavo":
    print("Que nome bonito!")

elif nome.lower() == "Pedro" or nome.lower() == "Maria" or nome.lower() == "Paulo":
    print("Seu nome é bem popular no Brasil.")

elif nome.lower() in 'Ana Cláudia Jéssica Juliana':
    print("Belo nome feminino.")

else:
    print("Seu nome é bem normal.")
    
print("Tenha um bom dia, {}!".format(nome))