# Crie um programa onde o usuário digite uma expressão
# qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados
# na ordem correta.

exp = input("Digite a expressão: ")

if exp.count("(") == exp.count(")"):
    print("Sua expressão está válida.")
else:
    print("Sua expressão é inválida.")