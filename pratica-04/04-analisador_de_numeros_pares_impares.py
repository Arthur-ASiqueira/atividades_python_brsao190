"""

4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.

"""

pares = 0
impares = 0

for entrada in range(1000):
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada == "fim":
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Número par.")
            pares += 1
        else:
            print("Número ímpar.")
            impares += 1
    except ValueError:
        print("Erro: digite um número inteiro válido.")

print()
print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")
