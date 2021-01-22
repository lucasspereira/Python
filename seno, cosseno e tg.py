# Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan
angulo = int(input('Digite um valor: '))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print('O seno de {} é {}. O cosseno de {} é {}. E a tangente de {} é {}.'.format(angulo, seno, angulo, cosseno, angulo, tangente))

# Resolução:
import math
a = float(input("Digite o ângulo que você deseja: "))
print("Seno: {:.2f}".format(math.sin(math.radians(a))))
print("Cosseno: {:.2f}".format(math.cos(math.radians(a))))
print("Tangente: {:.2f}".format(math.tan(math.radians(a))))