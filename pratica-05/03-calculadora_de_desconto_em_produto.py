"""

3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.

"""

preco_original = float(input("Digite o preço original do produto: R$ "))

desconto_desejado = float(input ("Digite o percentual de desconto desejado: "))

def calculadora_desconto(final):
    final = preco_original * (1 - desconto_desejado / 100)
    return final

preco_final = calculadora_desconto(preco_original)
print(f"O preço final do produto com desconto é: R$ {preco_final:.2f}")