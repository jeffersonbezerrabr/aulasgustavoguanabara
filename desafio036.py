#Escreva um programa para aprovar o empréstimo bancário para
#a compra de uma casa. O programa va iperguntar o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não
#pode exceder 30% do salário ou então empréstimo será negado.

casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o valor do seu salário? "))
anos = int(input("Deseja pagar em quantos anos? "))

parcelas = anos * 12
valor_prestacao = casa / parcelas

if valor_prestacao < salario * 0.30:
    print("Emprestimo aprovado!")
    print(f"\nValor da prestação R${valor_prestacao:.2f}")
else:
    print("Emprestimo negado.")