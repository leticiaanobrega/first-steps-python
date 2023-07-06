d=int(input('Quantos dias alugados?'))
k=float(input('Quantos Km rodados?'))
total=(d*60)+(k*0.15)
print(f'O total a pagar é de R${total:.2f}')