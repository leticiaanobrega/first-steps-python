import random
p=input('Primeiro aluno: ')
s=input('Segundo aluno: ')
t=input('Terceiro aluno: ')
q=input('Quarto aluno: ')
alunos=[p,s,t,q]
{random.shuffle(alunos)}
print(f'A ordem de apresentação será: {alunos}')