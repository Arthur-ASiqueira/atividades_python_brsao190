"""

3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.

"""
import requests

cep = input("Digite o CEP (apenas números, sem traço): ")

try:
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    response.raise_for_status()  

    dados = response.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        logradouro = dados['logradouro']
        bairro = dados['bairro']
        cidade = dados['localidade']
        cep = dados['cep']
        print(f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nCEP: {cep}")

except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
