"""

3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".

"""
for senha in range(1000):  
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha == "sair":
        print("Programa encerrado pelo usuário.")
        break


    if len(senha) < 8:
        print("Senha fraca. Ela deve ter pelo menos 8 caracteres.")
        print()  # pula uma linha
        continue


    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("Senha fraca. Ela deve conter pelo menos um número.")
        print()  # pula uma linha
        continue

    print("Senha forte!")
    break
