distancia = float(input('Informe e distância da viagem:'))
if distancia <= 200:
    preco = distancia*0.5
else:
    preco = distancia*0.45
print(f'O valor da passagem é de R${preco:.2f}')