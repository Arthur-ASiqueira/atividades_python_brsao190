"""

1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.

"""

def calcular_gorejeta(valor, porcentagem):
    return valor * (porcentagem / 100)

valor = 200
porcentagem = 15

gorjeta = calcular_gorejeta(valor, porcentagem)
print(f"{gorjeta:.2f}")