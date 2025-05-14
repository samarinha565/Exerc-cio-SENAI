produto = input("Produto: ")
valor_total = float(input("Preço: "))
porcentagem = float(input("Porcentagem de desconto: "))
desconto = valor_total * (porcentagem/100)
valor_novo = valor_total-desconto
print("O ", produto,'com R$',desconto, 'de desconto ficará por R$', valor_novo)
print(f'O {produto} com R${desconto} de desconto ficará por R${valor_novo}')
