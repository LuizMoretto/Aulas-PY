# Estruturas condicionais com validação simples (em string)
'''
nome = input('Digite o seu nome: ')

if nome == 'Fernando':
    print('Olá Fernando, você é o administrador do sistema!!!')
else nome in 'Ana-Barbara-Carlos-José-Maria-Paulo-Tatiana':
    print(
        f'Bem vindo(a) {nome}, você é um(a) usuário(a) registrado no sitema.')
else:
    print('Olá, você não está logado no sistema, suas permissões são restritas.')
'''

# Outra maneira de fazer de forma correta

nome = input('Digite seu nome: ')

funcionarios_homens = ['Carlos', 'José', 'Paulo']
funcionairos_mulheres = ['Ana', 'Bárbara', 'Maria', 'Tatiana']

if nome == 'Fernando':
    print('olá Fernando, você é o administrador do sistema!!!')
elif nome in funcionairos_mulheres:
    print(f'Bem vinda {nome}, você é uma usuária registrada no sistema.')
elif nome in funcionarios_homens:
    print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
else:
    print('Olá, você não está logado no sistema, suas permissões são restritas.')
