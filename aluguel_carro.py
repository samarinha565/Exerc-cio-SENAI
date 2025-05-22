
# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado


# 1 - (dias) Pedir a quantidade de dias
# 2 - (km) Pedir a quantidade de km percorridos

# 3 - (valor_dias) Calcular o valor total dos dias (dias * 60)
# 4 - (valor_km) Calcular o valor total da quilometragem (km * 0.15)


# 5 - (valor_total) Calcular o valor total somando o valor dos dias + o valor dos km

# 6 - Mostrar na tela a frase formatada

carro = input("Qual o modelo do carro alugado? ")




dias = int(input("Quantos dias ficou com carro? "))
km = float(input("Quantos km percorridos ? "))
valor_dia = 0
if carro == "uno":
    valor_dia = 30

elif carro =="celta":
    valor_dia = 25

else:
    valor_dia = 60

valor_dias = (dias * valor_dia)
valor_km = (km * 0.15)
valor_total = valor_dias + valor_km 
print(f"Você andou {km}km por {dias} dias, então o preço a pagar é R${valor_total}")