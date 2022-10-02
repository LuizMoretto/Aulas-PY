#Estudo de funções aritméticas

n1 = int(input('Adicione um valor'))
n2 = int(input('Outro valor: '))
s = n1 + n2 #soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisão
di = n1 // n2 #sobra da divisão
e = n1 ** n2 #potencia
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>>')
print('Divisão inteira {} e potência {}'.format(di,e))