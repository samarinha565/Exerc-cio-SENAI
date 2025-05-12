from colorama import init, Fore
init(autoreset=True)


print("|",30*'-',"|")
print('| SISTEMA DE PROVAS')
print('|',30*'-',"|")

nome = input('| Nome do aluno: ')
n1 = float(input('| Nota da primeira prova: '))
n2 = float(input('| Nota da segunda prova: '))
n3 = float(input('| Nota da terceira prova: '))
print("|",30*'-',"|")
media = round((n1+n2+n3) /3, 2)  # round(calculo, número de casas decimais) round(media, 2)
print('|Aluno:', nome,'\n|Média:',media)
if media >=5:
    print('|',Fore.GREEN + 'Aluno aprovado')
else:
    print('|',Fore.RED + 'Aluno reprovado')
print("|",30*'-',"|")

    
