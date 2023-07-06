velocidade = float(input('Informe a velocidade atual do carro: '))
multa = (velocidade-80)*7
if velocidade>=80:
    print(f'O carro excedeu o limite de 80km/h e foi multado em R${multa}')
print ('Tenha um bom dia, dirija com segurança')