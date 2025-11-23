#Curso Python #09 - Manipulando Texto

frase = "Curso em Vídeo Python"
print(frase)
print(frase[9:])
print(frase[::])
print(frase[:9])
print(frase[9::2])
print(frase[::2])
print(len(frase))
print(frase.count("o"))
print(frase.count("o", 0, 13))
print(frase.find("deo"))
print(frase.find("Android"))
print("Curso" in frase)
print(frase.replace("Python", "Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = "   Aprenda Python  "
print(len(frase))
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

frase = "Curso em Vídeo Python"
dividido = frase.split()
print(len(dividido))
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[3])
print(dividido[2][3])
print("-".join(frase))