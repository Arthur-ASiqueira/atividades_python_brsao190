"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

produto = input("Digite o nome do produto: ")

preco = input("Digite o preço do produto: ")
preco = float(preco)

desconto = input("Digite a porcentagem de desconto: ")
desconto = float(desconto)

calculo_desconto = preco * (desconto / 100)

preco_final = preco - calculo_desconto

print(f"O preço do item {produto} é R$ {preco:.2f}, mas com o desconto de {desconto}%, o valor do desconto é R$ {calculo_desconto:.2f}, totalizando R$ {preco_final:.2f}.")


