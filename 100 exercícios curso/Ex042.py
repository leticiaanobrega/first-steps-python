print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b < c and b + c < a and a + c < b:
    print('Os segmentos podem formar um triângulo!')
    if a != b != c:
        print('E ele vai ser um triângulo escaleno!')
    elif a == b == c:
        print('E ele vai ser um triângulo equilátero!')
    elif a == b or a == c or b == c:
        print('E ele vai ser um triângulo isósceles!')
else:
    print('Os segmentos acima não podem formar um triângulo')
