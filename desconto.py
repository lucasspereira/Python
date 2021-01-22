# Faça um algoritmo que leia o preço de um produto e mostre seu preço com 5% de desconto

preco_real = float(input('Valor (R$):'))
preco_desc = preco_real *0.05
r = preco_real - preco_desc
print('O valor com desconto de 5% é R${:.2f}. Você economizou R${:.2f}'.format(r, preco_desc))