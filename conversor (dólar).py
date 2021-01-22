# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = int(input('Quanto dinheiro (em R$) você tem?'))
dolar = reais/5.13
print('Com R${}, você consegue comprar U${}'.format(reais, dolar))
