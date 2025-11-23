#Crie um programa que leia uma frase qualquer e diga
#se ela é um palindromo, desconsiderando os espaços.

'''frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split()
junto = "".join(palavras)
invertido = junto[::-1]
if junto == invertido:
    print("A frase é um palindromo:")
    print(f"{junto} é igual a {invertido}")
    
else:
    print("A frase não é palindromo")
    '''
    
frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split()
junto = "".join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print("A frase é um palindromo:")
    print(f"{junto} é igual a {inverso}")
    
else:
    print("A frase não é palindromo")