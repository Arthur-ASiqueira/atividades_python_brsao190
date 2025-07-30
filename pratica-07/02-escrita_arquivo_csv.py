"""

2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.

"""


import csv

arquivo_entrada = input("Digite o nome do arquivo CSV de origem (ex: dados_pessoas.csv): ")

arquivo_saida = input("Digite o nome do novo arquivo CSV para salvar os dados: ")

try:
    with open(arquivo_entrada, mode='r', encoding='utf-8') as entrada:
        leitor = csv.reader(entrada)
        dados = list(leitor)  

   
    with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as saida:
        escritor = csv.writer(saida)
        escritor.writerow(["Nome", "Idade", "Cidade"])
        escritor.writerows(dados)

    print(f"Dados gravados com sucesso no arquivo '{arquivo_saida}'.")

except FileNotFoundError:
    print(f"Erro: o arquivo '{arquivo_entrada}' não foi encontrado.")
except Exception as erro:
    print(f"Erro ao processar os arquivos: {erro}")
