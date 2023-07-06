numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão e digite a opção:
[ 1 ] - para converter o valor para binário
[ 2 ] - para converter o valor para hexadecimal
[ 3 ] - para converter o valor para octal''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'O número {numero} convertido para binário será {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} convertido para hexadecimal será {hex(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} convertido para octal será {oct(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
