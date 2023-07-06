import math
a=float(input('Digite o ângulo que você deseja: '))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print(f'O ângulo de {a} tem o SENO de {s:.2f} \nO ângulo de {a} tem o COSSENO de {s:.2f} \nO ângulo de {a} tem a TANGENTE de {t:.2f}')