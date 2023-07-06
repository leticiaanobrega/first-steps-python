preco = float(input('Informe o valor do produto: '))
formaDePagamento = str(input('O pagamento será feito em dinheiro, cheque ou cartão? ')).lower()

if formaDePagamento == 'cartão':
    parcelas=int(input(f'O pagamento por cartão permite o parcelamento desse valor.\n'
'Caso seja feito a vista, em 1 única parcela, será aplicado um desconto de 5%.\n'
'Caso seja feito em até 2x, o valor do produto permanece o mesmo, sem juros.\n'
'Caso seja feito em 3x ou mais, o valor do produto terá um juros de 20%\n'
'O pagamento será feito em quantas parcelas? '))
    if parcelas == 1:
        print(f'O valor do produto será de R${preco-(preco*0.05):.2f}.')
    elif parcelas == 2:
        print(f'O valor do produto será de R${preco:.2f}.')
    else:
        print(f'O valor do produto com juros será de R${preco+(preco*0.2):.2f}')
elif formaDePagamento == 'dinheiro':
    print(f'O valor do produto à vista em dinheiro possui 10% de desconto. Sendo assim, o valor total a pagar é de {preco-(preco*0.1):.2f}')
else:
    print(f'O valor do produto à vista no cheque possui 10% de desconto. Sendo assim, o valor total a pagar é de {preco-(preco*0.1):.2f}')