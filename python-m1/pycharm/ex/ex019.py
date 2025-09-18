# Import principais
from random import choice

print(f'Sistema de sorteio aleotorio por nome')
w = str(input('Pessoa 1: '))
x = str(input('Pessoa 2: '))
y = str(input('Pessoa 3: '))
z = str(input('Pessoa 4: '))
# Lembrar, quando for lidar com multiplus dados (mais de tres) usar lista, para poder usar a bib random do jeito certo
lista = [w, x, y, z]
escolido = choice(lista)
print(f'Parabens {escolido} você foi escolido!')
