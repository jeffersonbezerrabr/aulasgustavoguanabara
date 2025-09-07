# Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-os(com idade) em um
# dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {}

dados["nome"] = str(input("Nome: "))
ano_nascimento = int(input(f"Ano de nascimento: "))
idade = datetime.now().year - ano_nascimento
dados["idade"] = idade
dados["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if dados["ctps"] != 0:
    dados["contratacao"] = int(input("Ano de contratação: "))
    dados["salario"] = float(input("Salário: "))
    dados["aposentadoria"] = (dados["contratacao"] + 35) - ano_nascimento
    for k, v in dados.items():
        print(f"{k} tem o valor {v}")

else:
    for k, v in dados.items():
        print(f"{k} tem o valor {v}")