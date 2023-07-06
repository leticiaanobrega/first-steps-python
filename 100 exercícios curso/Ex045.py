from random import sample
print('=-='*7)
print('\033[45;36;1mVamos brincar de Jokenpô?!\033[m')
print('=-='*7)
maquina = sample(['pedra', 'papel', 'tesoura'],1)
usuario = str(input('Escolha: pedra papel ou tesoura? ')).lower()

if usuario == 'pedra' and maquina == 'papel':
   print(f'Você escolheu {usuario} e eu escolhi {maquina}! Ganhei!')
elif usuario == 'pedra' and maquina == 'tesoura':
    print(f'Você escolheu {usuario} e eu escolhi {maquina}! Você venceu!')
elif usuario == 'papel' and maquina == 'tesoura':
    print (f'Você escolheu {usuario} e eu escolhi {maquina}! Você me venceu!')
else:
    print (f'Você escolheu {usuario} e eu também escolhi {maquina}! Isso é um empate!')