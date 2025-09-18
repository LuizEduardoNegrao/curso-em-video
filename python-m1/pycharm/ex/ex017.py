# Principais importações
from math import hypot

print('Calcule os dois catetos a seguir para saber o valor ad hipotenusa')
# Nesse exercicio é importante usar o float para o resultado dar como flutuante, senao da erro, ate porque a hipotenusa (quase sempte) da como flutuante
a = float(input('cateto a: '))
b = float(input('cateto b: '))
h = hypot(a, b)
print(f'O valor da sua hipotenusa é: {h:.2f}')
