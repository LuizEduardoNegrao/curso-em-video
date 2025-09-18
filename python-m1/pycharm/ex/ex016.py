# Principais importações
from math import trunc, ceil

print('Transformando numero real em inteiro')
n = float(input('Digite um numero: '))
t = trunc(n)
a = ceil(n)
print(f'voce digitou o numero real: {n} e o seu numero inteiro é: {t} arredondando fica: {a}')
