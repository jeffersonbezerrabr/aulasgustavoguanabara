#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros

valor = float(input("Qual o valor da sua compra? R$ "))
print("""
    Digite 1 para: À vista dinheiro/cheque: 10% de desconto
    Digite 2 para: À vista no cartão: 5% de desconto
    Digite 3 para: Em até 2x no cartão: Preço normal
    Digite 4 para: 3x ou mais no cartão: 20% de juros
      """)
forma = int(input("Qual a forma de pagamento: "))

if forma == 1:
    valor_final = valor - (valor * 0.10)
    print(f"Você tem 10% de desconto. O valor ficará R$ {valor_final:.2f}")
elif forma == 2:
    valor_final = valor - (valor * 0.05)
    print(f"Você tem 5% de desconto. O valor ficará R$ {valor_final:.2f}")
elif forma == 3:
    valor_final = valor
    print(f"Em até 2x no cartão não tem desconto. O valor continua R$ {valor_final:.2f}")
elif forma == 4:
    valor_final = valor + (valor * 0.20)
    parcelas = int(input("Quantas parcelas? "))
    valor_parcela = valor_final / parcelas
    print(f"Sua compra será parcelada em {parcelas}x de R${valor_parcela} COM JUROS. O valor ficará R$ {valor_final:.2f}")
else:
    print("Opção invalida")