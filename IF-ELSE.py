# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km
# para viagens de até 200km e R$0,45para viagens mais longas.

distancia = float(input('Qual é a distancia da viagem (em km)? '))
if distancia <=200:
    viagem_curta = distancia*0.5
    print('Sua passagem custará R${:.2f}'.format(viagem_curta))
else:
    viagem_longa = distancia*0.45
    print('Sua passagem custará R${:.2f}'.format(viagem_longa))