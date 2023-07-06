valorImovel = float(input('Informe o valor do imóvel: R$'))
salario = float(input('Informe o salário do comprador: R$'))
anosDePagamento = int(input('Informe em quantos anos o imóvel será pago: '))

mesesDePagamento = anosDePagamento * 12
mensalidade = valorImovel / mesesDePagamento
print(f'Sua mensalidade será de R${mensalidade:.2f}.')

if mensalidade <= salario*0.3:
    print(f'Com o salário de R${salario:.2f}, seu financiamento está aprovado.')
else:
    print(f'Infelizmente as parcelas excederam 30% de seu salário e seu financiamento não pôde ser aprovado.')
