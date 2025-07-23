"""

3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""
informar = input("Informe a temperatura: ")
informar = float(informar)

unidade_origem = input("Informe a temperatura atual: ")
unidade_destino = input("Informe a a temperatura que quer converter: ")

if unidade_origem == 'Celsius' and unidade_destino == 'Fahrenheit':
    conversao = (informar * 9/5) + 32
    print(f"{informar}° Celsius é igual a {conversao}° Fahrenheit.")

elif unidade_origem == 'Celsius' and unidade_destino == 'Kelvin':
    conversao = informar + 273.15
    print(f"{informar}° Celsius é igual a {conversao} Kelvin.")

elif unidade_origem == 'Fahrenheit' and unidade_destino == 'Celsius':
    conversao = (informar - 32) * 5/9
    print(f"{informar}° Fahrenheit é igual a {conversao}° Celsius.")

elif unidade_origem == 'Fahrenheit' and unidade_destino == 'Kelvin':
    conversao = (informar - 32) * 5/9 + 273.15
    print(f"{informar}° Fahrenheit é igual a {conversao} Kelvin.")

elif unidade_origem == 'Kelvin' and unidade_destino == 'Celsius':
    conversao = informar - 273.15
    print(f"{informar} Kelvin é igual a {conversao}° Celsius.")

elif unidade_origem == 'Kelvin' and unidade_destino == 'Fahrenheit':
    conversao = (informar - 273.15) * 9/5 + 32
    print(f"{informar} Kelvin é igual a {conversao}° Fahrenheit.")

