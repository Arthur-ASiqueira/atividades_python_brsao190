"""

2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"

"""

peso = input("Informe seu peso em Kg: ")
peso = float(peso)

altura = input("Informe sua altura em metros: ")
altura = float(altura)

calculo_imc = peso / altura ** altura

if calculo_imc >= 0 and calculo_imc < 18.5:
    print("Classificação: Abaixo do peso")

elif calculo_imc > 18.5 and calculo_imc < 25:
    print("Classificação: Sobrepeso")

elif calculo_imc > 25 and calculo_imc < 30:
    print("Classificação: Sobrepeso")

elif calculo_imc :
    print("Classificação: Obeso")