#inserindo o primeiro número (n1) e o segundo número (n2)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

#comparando os números
if n1 > n2:
    print(f'O primeiro valor digitado é maior')
elif n1 < n2:
    print(f'O segundo valor digitado é maior')
else:
    print(f'Não existe um valor maior, os dois valores são iguais')

