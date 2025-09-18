from random import shuffle

print('Sistema de sorteio aleatorio por nome que mosta a ordem sorteada')
a = input('Nome da primeira pessoa: ')
b = input('Nome da segunda pessoa: ')
c = input('Nome da terceira pessoa: ')
d = input('Nome da quarta pessoa: ')
# O suffle(lista) embaralha a lista diretamente
lista = [a, b, c, d]
shuffle(lista)
print(f'A ordem foi {lista}, respectivamente do primeiro ao ultimo')
