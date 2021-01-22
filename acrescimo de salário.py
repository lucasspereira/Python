# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome_funcionario = input('Funcionário:')
salario = float(input('Salário:'))
novo_salario = salario *0.15 + salario
print('Parabéns, {}!!! Você ganhou 15% de aumento. Agora seu salário é {:.2f}'.format(nome_funcionario, novo_salario))
