"""

3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

"""

nota1 = input("Digite a nota 1: ")  
nota1 = float(nota1)

nota2 = input("Digite a nota 2: ")
nota2 = float(nota2)

nota3 = input("Digite a nota 3: ")
nota3 = float(nota3)

calculo_media = (nota1 + nota2 + nota3) / 3

print(f"As notas do aluno são: {nota1:.2f}, {nota2:.2f}, {nota3:.2f}.")
print(f"A média final do aluno é: {calculo_media:.2f}.")