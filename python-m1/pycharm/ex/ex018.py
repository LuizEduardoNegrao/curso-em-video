# Principais importações
from math import sin, cos, tan, radians

print('Digite um angulo qualuqer para saber seu seno, cosseno e tangente')
a = float(input('digite um angulo: '))
# o rad é importante porque garante que o ângulo digitado em graus seja convertido para radianos, que é a “linguagem” que o Python entende para cálculos trigonométricos.
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print(f'seu angulo é: {a:.3f}°, seu seno é {s:.3f}, cosseno {c:.3f} e tangente {t}')
