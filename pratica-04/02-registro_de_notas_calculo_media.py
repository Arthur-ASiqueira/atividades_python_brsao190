"""

2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.  

"""

notas = []

for _ in range(1000):  # número grande para simular um loop "infinito"
    entrada = input("Digite uma nota entre 0 e 10 (ou 'fim' para encerrar): ")

    if entrada == "fim":  # aqui só aceita exatamente "fim"
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Erro: a nota deve estar entre 0 e 10.")
    except ValueError:
        print("Erro: entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f}")
    print(f"Total de notas válidas: {len(notas)}")
else:
    print("\nNenhuma nota válida foi registrada.")

