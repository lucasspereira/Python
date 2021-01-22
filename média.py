# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome_aluno = input('Nome do aluno:')
ra = input('RA:')
n1 = float(input('Nota avaliação 1:'))
n2 = float(input('Nota avaliação 2:'))
media = float((n1 + n2)/2)
print('A média do aluno {} de RA {} é {}'.format(nome_aluno, ra, media))
