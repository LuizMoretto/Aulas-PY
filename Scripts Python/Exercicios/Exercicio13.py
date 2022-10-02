salario = float(input('Entre com o valor do salário: '))
aumento = float(input('Quantos % você deseja dar de aumento? '))

novosalario = salario + (salario * (aumento/100))

print('O novo salario do funcionário é de : {:.2f}'.format(novosalario))