#coletando os dados das notas (n1 e n2):
n1 = float(input('Informe a nota do primeiro semestre: '))
n2 = float(input('Informe a nota do segundo semestre: '))

#calculando a média:
media = (n1 + n2)/2

if media < 5:
    print('REPROVADO')
elif media >= 7:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')