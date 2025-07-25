"""

4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.

"""

ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = 2025

def calculadora_idade_em_dias(ano_nascimento, ano_atual):
    idade_em_anos = ano_atual - ano_nascimento
    idade_em_dias = idade_em_anos * 365
    return idade_em_dias

dias = calculadora_idade_em_dias(ano_nascimento, ano_atual)

print(f"Você tem {dias} dias de idade.")