# Estruturas condicionais com interpolação

nomes = ['Fernando', 'Maria', 'Carlos']

usuario = input('Digite o seu nome: ')

if usuario in nomes:
    print(f'Bem vindo(a) {usuario}')
else:
    print('Usuário não cadastrado.')
