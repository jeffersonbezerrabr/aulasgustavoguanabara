#Crie um programa que faça o computador
#jogar Jokenpô com você.

from random import randint

print("Vamos jogar pedra, papel e tesoura.")
x = 0
y = 0 
while True:
    jog = int(input("""
Digite 1 para pedra
Digite 2 para papel
Digite 3 para tesoura
Digite 0 para sair: \n"""))
    pc = randint(1,3)
    if jog == 0:
        print("Encerrando programa...")
        break
    
    if jog == 1 and pc == 1:
        print("Você e o Pc escolheram pedra. Deu empate.")
        print("_-_" * 24)
    elif jog == 1 and pc == 2:
        print("""
Você escolheu Pedra!
O PC escolheu Papel!
Papel embrulha a pedra!
1 ponto para o PC!""")
        print("_-_" * 24)
        x += 1
    elif jog == 1 and pc == 3:
        print("""
Você escolheu Pedra!
O PC escolheu Tesoura!
Pedra quebra Tesoura!
1 ponto para o você!""")
        print("_-_" * 24)
        y += 1
    elif jog == 2 and pc == 1:
        print("""
Você escolheu Papel!
O PC escolheu Pedra!
Papel embrulha a pedra!
1 ponto para o você!""")
        print("_-_" * 24)
        y += 1
    elif jog == 2 and pc == 2:
        print("Você e o PC escolheram Papel. Deu empate.")
        print("_-_" * 24)
    elif jog == 2 and pc == 3:
        print("""
Você escolheu Papel!
O PC escolheu Tesoura!
Tesoura corta papel!
1 ponto para o PC!""")
        print("_-_" * 24)
        x += 1
    elif jog == 3 and pc == 1:
        print("""
Você escolheu Tesoura!
O PC escolheu Pedra!
Pedra quebra Tesoura!
1 ponto para o PC!""")
        print("_-_" * 24)
        x += 1
    elif jog == 3 and pc == 2:
        print("""
Você escolheu Tesoura!
O PC escolheu Papel!
Tesoura corta Papel!
1 ponto para o você!""")
        print("_-_" * 24)
        y += 1
    elif jog == 3 and pc == 3:
        print("Você e o PC escolheram Tesoura. Deu empate.")
    else:
        print("Opção invalida! Digite 1,2,3 ou 0 para sair.")

print(f"O PC fez {x} pontos")
print(f"Você fez {y} pontos")
   
if x > y:
    print("O computador venceu.")
elif x == y:
    print("Empatou.")
else:
    print("Você venceu!")

print("Até a proxima")