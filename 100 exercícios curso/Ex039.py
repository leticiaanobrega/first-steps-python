from datetime import date
#Coletando os dados
anoDeNascimento = int(input('Informe seu ano de nascimento: '))

#Calculando o tempo para alistamento
idade =  date.today().year - anoDeNascimento

if idade > 18:
    prazoExcedente = idade - 18
    print(f'Seu prazo para se alistar está atrasado. Você está a {prazoExcedente} ano(s) atrasado.')
elif idade < 18:
    prazo = 18 - idade
    print(f'Você ainda possui {prazo} ano(s) até precisar se alistar.')
else:
    print(f'Você está na idade exigida para alistamento.')