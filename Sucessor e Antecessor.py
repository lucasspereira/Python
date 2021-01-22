# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número:'))
ant = n1 - 1
suc = n1 + 1
print('O antecessor de {} é {}.'.format(n1, ant), end= ' O sucessor de {} é {}.'.format(n1, suc))