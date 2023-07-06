peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso/(altura*altura)

if imc < 18.5:
    print(f'Atenção! Seu IMC é de {imc:.2f} e você está abaixo do seu peso ideal. Consulte um médico!')
elif imc <= 25:
    print(f'Ótimo! Seu IMC é de {imc:.2f} e você está em seu peso ideal!')
elif imc <= 30:
    print(f'Atenção! Seu IMC é de {imc:.2f} e você está entrando na faixa do sobrepeso.')
elif imc <= 40:
    print(f'Atenção! Seu IMC é de {imc:.2f} e já caracteriza obesidade. Consulte um médico!')
else:
    print(f'Atenção! Seu IMC é de {imc:.2f} e caracteriza obesidade mórbida. Consulte um médico!')