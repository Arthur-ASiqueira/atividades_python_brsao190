"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

"""

dinheiro_real = input("Digite o valor em reais (R$): ")
dinheiro_real = float(dinheiro_real)

calculadora_dolar = dinheiro_real / 5.20
calculadora_euro = dinheiro_real / 6.15

print(f"Seu dinheiro convertido em dólares é: ${calculadora_dolar:.2f}")
print(f"Seu dinheiro convertido em euros é: €{calculadora_euro:.2f}")
print("Finalizado a conversão de moeda.")