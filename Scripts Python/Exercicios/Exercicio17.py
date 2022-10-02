import math
ca = float(input('Entre com o Cateto Adjacente: '))
co = float(input('Entre com o Cateto Oposto '))

hip = float((ca * ca)+(co * co))
res = float(math.sqrt(hip))

print('{:.2f}'.format(res))
