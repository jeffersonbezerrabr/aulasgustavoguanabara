#Faça um algoritimo que leia o preço de um produto e mostre
#seu novo preço, com 5% de desconto.

preco_produto = float(input("Qual o valor do produto: "))

desconto = preco_produto * 0.05
preco_desconto = preco_produto - desconto
print(f"O preço do produto com 5% de desconto é R$ {preco_desconto:.2f}")