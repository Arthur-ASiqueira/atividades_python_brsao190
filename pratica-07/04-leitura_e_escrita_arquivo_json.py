"""

4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.



"""

import json

dados_pessoa = {
    "nome": "Ana Costa",
    "idade": 30,
    "cidade": "Salvador"
}

nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

try:
    with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo_json:
        json.dump(dados_pessoa, arquivo_json, indent=4, ensure_ascii=False)
    print(f"\nDados salvos com sucesso no arquivo '{nome_arquivo}'.")

    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_json:
        dados_lidos = json.load(arquivo_json)
        print("\nConteúdo lido do arquivo:")
        print(dados_lidos)

except FileNotFoundError:
    print(f"Erro: o arquivo '{nome_arquivo}' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro: o arquivo não contém um JSON válido.")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
