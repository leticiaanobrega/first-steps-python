nomeCompleto = str(input('Digite seu nome completo: ')).strip().split()
primeiroNome = nomeCompleto[0]
nomeInvertido = nomeCompleto[::-1]
ultimoNome = nomeInvertido[0]
print(f'Muito prazer em te conhecer! \nSeu primeiro nome é {primeiroNome} \nSeu último nome é {ultimoNome}')
