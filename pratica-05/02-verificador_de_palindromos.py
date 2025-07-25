"""

2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.

"""

def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

frase = "A cara rajada da jararaca"  
palindromo = verificar_palindromo(frase)

if verificar_palindromo(frase):
    print(f"{frase} é um palíndromo.")
else:
    print(f"{frase} não é um palíndromo.")

