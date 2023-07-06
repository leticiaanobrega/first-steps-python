import random
import time
numeroComputador = random.randint(0,5)
print('-=-'*20,'\nVou pensar em um número entre 0 e 5. Tente adivinhar...\n', '-=-'*20)
numeroJogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if numeroComputador == numeroJogador:
    print('PARABÉNS! Você adivinhou!')
else:
    print(f'Perdeu! Estava pensando no número {numeroComputador} e não no {numeroJogador}!')
