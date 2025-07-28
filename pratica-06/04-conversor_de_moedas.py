"""

4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.

"""

import requests

cotacao = input("Digite a cotação (USD, EUR, GBP): ")

response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{cotacao}-BRL")

if response.status_code == 200:
    dados = response.json()['USDBRL'][0]
    valor_minimo =  dados['low']
    valor_maximo = dados['high']
    data = dados['create_date']
    print(f"Valor Minimo: {valor_minimo}\nValor Maximo: {valor_maximo}\nData: {data}")
else:
    print(f"Requisição falhou. Código de erro: {response.status_code}")