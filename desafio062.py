#Melhore o desafio 61, perguntando para o usuário se ele quer mostrar
#mais alguns termos. O programa encerra quando
#ele disser que quer mostrar 0 termos.

x = 1
termo = int(input("Termo: "))
razao = int(input("Razão: "))
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while x <= total:
        print(f"{termo} > ", end='')
        termo += razao
        x += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM")
print(f"Progressão finalizada com {total} termos mostrados.")
