# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
num = float(input('Digite um número: '))
result = trunc(num)
print('A porção inteira de {} é {}'.format(num, result))

