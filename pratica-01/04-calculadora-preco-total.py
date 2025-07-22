"""

4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

"""

nome_produto = "Cadeira Infantil"
preco = 12.40
quantidade = 3

calculadora_de_preco = preco * quantidade

print("Nome do Produto:", nome_produto)
print(f"Preço Unitário: R$ {preco:.2f}")
print("Quantidade", quantidade)
print(f"Preço Total: R$ {calculadora_de_preco:.2f}")

# oi