from datetime import datetime

now = datetime.now()

nome = 'Gui'
idade = 23
altura = 1.75
peso = 60
ano = now.strftime('%Y')
imc = peso / (altura ** 2)
nascimento = int(ano) - idade

print(f'{nome} tem {idade} anos de idade e {altura} de altura')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'O {nome} nasceu em {nascimento}')
