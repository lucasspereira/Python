# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o
# nome do escolhido.

import random
a1 = input('Digite um aluno: ')
a2 = input('Digite outro: ')
a3 = input('Digite outro: ')
a4 = input('Digite outro: ')
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)
print('O aluno escolhido para apagar a louza é o(a) {}'.format(sorteado))
