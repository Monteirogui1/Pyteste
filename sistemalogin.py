usuario = input('Usuario: ')
senha = input('Senha: ')

usario_bd = 'Gui'
senha_bd = '1234'

if usuario == usario_bd and senha == senha_bd:
    print('Entrou!')
else:
    print('Usuario ou Senha incorreta.')
