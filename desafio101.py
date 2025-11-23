# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPICIONAL ou
# OBRIGATÓRIO nas eleições.

def voto(num):
    from datetime import date
    idade = date.today().year - ano_nasc
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif idade >= 18 and idade < 65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."
    else:
        return f"Com {idade} anos: VOTO OPCIONAL."
             

ano_nasc = int(input("Em que ano você nasceu? "))
print(voto(ano_nasc))
