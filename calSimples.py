num_1 = input('Digite um numero: ')
num_2 = input('Digite um numero: ')

print('Digite a operação:\n\t+ para Adição\n\t- para Subtração\n\t* para Multiplicação\n\t/ para Divisão')

operacao = input('Digite a operação: ')

equacao = f'{num_1} {operacao} {num_2}'

resultado = eval(equacao)

print(f'{"*" * 25}\nResultado: {resultado}\n{"*" * 25}')
