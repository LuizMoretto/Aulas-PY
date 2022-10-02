# Estrutura de repetição

# While
'''
variavel = 0

while variavel <= 5:
    print(variavel)

    variavel += 1
'''
#===============================================#
'''

num = 0
total = 10

while num <= 10:
    print(num)
    num += 1

    if num == 5:
        print('50% computado')
    if num == total:
        print('100%, processo encerrado')
'''

#================================================#
'''
validador = input('Digite "Brasil" para continuar:')

while validador != 'Brasil':
    print('Palavra-chave não confere, digite novamente:')
    validador = input('Digite "Brasil" para continuar:')

    if validador == 'Brasil':
        print('Agora você digitou brasil corretamente.')
'''
#================================================#

while True:
    validador = input('Digite "Brazil" para continuar:')
    if validador == 'Brazil':
        print('você digitou Brazil corretamente!!!')
        break
    else:
        print('Palavra-Chave não confere, digite novamente:')
