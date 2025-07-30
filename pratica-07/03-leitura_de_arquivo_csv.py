"""

3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.

"""

import csv


nome_arquivo = input("Digite o nome do arquivo CSV que deseja ler (ex: dados.csv): ")

try:

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)

        print("\nConteúdo do arquivo:")
        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as erro:
    print(f"Ocorreu um erro ao ler o arquivo: {erro}")
