salario = float(input('Informe seu salário: R$ '))
if salario >= 1250:
    novoSalario = (salario*0.1) + salario
else:
    novoSalario = (salario*0.15) + salario
print(f'Seu salário com aumento será de R${novoSalario:.2f}')