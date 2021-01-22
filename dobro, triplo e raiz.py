# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número:'))
dn1 = n1 * 2
tn1 = n1 * 3
rn1 = n1**(1/2)
print('O dobro de {} é {}.'.format(n1, dn1), end='O triplo de {} é {}.'.format(n1, tn1))
print(' \nJá a raiz quadrada de {} é {}'.format(n1, rn1))