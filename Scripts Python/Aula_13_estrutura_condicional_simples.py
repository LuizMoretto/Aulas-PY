# Estrutura Condicional Simples

# IF

nome = input('Digite seu nome')

if nome == 'Fernando':
    print('Bem vindo de volta Fernando!!!')

print(f'Você é novo(a) aqui, Olá {nome}!!!')


# Se a condição for atingida, o bloco dela é executado,
# Caso contrario é simplesmente ignorado

# Estrutura com argumentos lógicos

num = 51

if num <50:
    print('Menor que 50')
else:
    print('Maior que 50')


# Estrutura com condicional Composta

num = input('Digite seu nome: ')

if nome == 'Fernando':
    print('Bem vindo de volta Fernando!!!')
else:
    print('Você não é Fernando...')

# Estruturas condicionais alinhadas

num1 = float(input('Digite um número: '))

if num1 <= 50:
    print('Menor que 50')
elif num1 > 50 and num1 < 100:
    print('Maior que 50')
else:
    print('Número Inválido')