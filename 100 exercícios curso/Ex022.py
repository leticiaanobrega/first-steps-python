nome=str(input('Digite seu nome completo:'))
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separado=nome.split()
print (f'Seu primeiro nome é {separado[0]}')
print (f'Seu primeito nome tem {len(separado[0])} letras')

