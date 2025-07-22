"""

4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""

distancia_percorrida = input("Digite a distância percorrida (km): ")
distancia_percorrida = float(distancia_percorrida)

combustivel_gasto = input("Digite o combustível gasto (litros): ")
combustivel_gasto = float(combustivel_gasto)

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"A distância percorrida foi de {distancia_percorrida:.2f} km.")
print(f"O combustível gasto foi de {combustivel_gasto:.2f} litros.")
print(f"O consumo médio do veículo é de {consumo_medio:.2f} km/l.")