contador = 1
provas = float(input('Quantas provas foram aplicadas? '))
soma = 0
while contador <= provas:
    print(contador)
    nota = float(input(f'Digite a nota da prova {contador}: '))
    soma = soma + nota
    contador = contador+1
    
media = (soma/provas)
print(f'Sua média final é de {media}.')    

