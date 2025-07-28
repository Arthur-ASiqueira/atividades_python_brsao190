"""

1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.

"""
import random
import string

# Solicita o tamanho da senha ao usuário
tamanho = int(input("Digite o tamanho da senha desejada: "))

letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = "!@#$%&*"

todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos


senha = [
    random.choice(letras_maiusculas),
    random.choice(letras_minusculas),
    random.choice(numeros),
    random.choice(simbolos)
]


while len(senha) < tamanho:
    senha.append(random.choice(todos_caracteres))


random.shuffle(senha)

senha_final = ''.join(senha)

print("Senha gerada:", senha_final)
