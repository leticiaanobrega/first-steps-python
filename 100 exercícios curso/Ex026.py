frase = str(input('Digite uma frase: ')).strip().upper()
repeticoesLetraA = frase.count('A')
posicaoPrimeiraLetraA = frase.find('A')+1
posicaoUltimaLetraA = frase.rfind('A')+1
print(f'A letra A aparece {repeticoesLetraA} vezes na frase. \nA primeira letra A aparece na posição {posicaoPrimeiraLetraA} \nA última letra A apareceu na posição {posicaoUltimaLetraA}')