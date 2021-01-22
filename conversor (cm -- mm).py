# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = int(input('Digite a quantidade de metros:'))
cm = metros*100
mm = metros*1000
print('{} metros equivale à {} centimetros e à {} milímetros'.format(metros, cm, mm)) 