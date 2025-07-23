"""

1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).

"""
idade = input("Digite sua Idade: ")
idade = int(idade)

if idade >= 0 and idade <= 12:
    print(f"Você tem {idade} anos e é uma Criança.")

elif idade >= 13 and idade <= 17:
    print(f"Você tem {idade} anos e é um Adolescente.")

elif idade >= 18 and idade <= 59:
    print(f"Você tem {idade} anos e é um Adulto.")

elif idade >= 60:
    print(f"Você tem {idade} anos e é um Idoso.")   
