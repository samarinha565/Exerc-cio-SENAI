nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
if idade >=18:
    print("Maior de Idade")
    carteira = int(input("Possui  carteira de montorista?(1-sim / 2-não)"))
    if carteira == 1:
     print("Pode dirigir")
    else: 
       print("Não pode dirigir")
else:
    print("Menor de Idade")
