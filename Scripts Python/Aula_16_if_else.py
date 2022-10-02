nome1 = 'Fernando'
nome2 = 'Maria'

if nome1 == 'Fernando':
    print('Bem-vindo Fernando!!!')
elif nome1 == 'Maria':
    print('Bem-vindo Maria!!!')
else:
    print('Erro: Nome Desconhecido')


# 2 ou mais condições sendo verdadeiras

num1 = 12
num2 = 44
nome1 = 'Fernando'
nome2 = 'Maria'

if num1 >= 10 and nome1 == 'Fernando':
    print('número mair que 10 e o usuário é fernando')
if num1 <= 10 and nome1 == 'Fernando':
    print('número mair que 10 e o usuário é fernando')
if num1 == 10 and nome1 == 'Fernando':
    print('número mair que 10 e o usuário é fernando')
if num1 != 10 and nome1 == 'Fernando':
    print('número mair que 10 e o usuário é fernando')

# Operador and exige que as duas condições sejam verdadeiras uma condição e outra.
