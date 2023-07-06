from datetime import date
anoDeNascimento = int(input('Ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento

if idade <= 9:
    print(f'Idade do atleta: {idade} \nCategoria: Mirim')
elif idade <= 14:
    print(f'Idade do atleta: {idade} \nCategoria: Infantil')
elif idade <= 19:
    print (f'Idade do atleta: {idade} \nCategoria: Júnior')
elif idade <= 20:
    print (f'Idade do atleta: {idade} \nCategoria: Sênior')
else:
    print (f'Idade do atleta: {idade} \nCategoria: Master')