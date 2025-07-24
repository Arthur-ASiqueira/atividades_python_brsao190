"""

1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.

"""
try:
    numero1 = input("Digite o primeiro número: ")
    numero1 = int(numero1)

    numero2 = input("Digite o segundo número: ")
    numero2 = int(numero2)
    
    operacao = input("Digite a operação desejada (+, -, *, /): ")

except ValueError:
    print("Entrada inválida. Por favor, insira números válidos.")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado de {numero1} + {numero2} é: {resultado}")


elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado de {numero1} - {numero2} é: {resultado}")

elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado de {numero1} * {numero2} é: {resultado}")
    
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado de {numero1} / {numero2} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")


