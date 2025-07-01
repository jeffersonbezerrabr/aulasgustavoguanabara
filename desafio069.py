# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar.
# No final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

x = 0
y = 0
maior = 0
while True:
    print("Cadastre uma pessoa")
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F]").upper().strip()[0]
    validar_continuar = "SN"
    validar_sexo = "MF"
    
    if sexo not in validar_sexo:
        print("Valor invalido! Digite M ou F")
        continue
    if sexo == "M":
        x += 1
    if idade > 18:
            maior += 1
    if sexo == "F" and idade < 20:
            y += 1
    continuar = input("Quer continuar? [S/N]").upper().strip()[0]
    if continuar not in validar_continuar:
        print("Valor invalido. Digite S ou N")
        continue
    if continuar == "S":
        continue
       
    if continuar == "N":
        print("Fim do Programa")
        break

print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f"Ao todo temos {x} homens cadastrados")
print(f"E temos {y} mulheres com menos de 20 anos.")