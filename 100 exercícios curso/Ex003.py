import math
n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
soma = n1+n2
print(f'A soma entre {n1} e {n2} é igual a {soma}')
arredondamentoCima = math.ceil(soma)
arredondamentoBaixo = math.floor(soma)
print(f'Arredondando esse valor para cima, temos um total de {arredondamentoCima} e, arredondando para baixo, temos um valor de {arredondamentoBaixo}')