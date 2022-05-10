# def calculadora(num1, op, num2):
#
#         if op == '+':
#             return num1 + num2
#         elif op == '-':
#             return num1 - num2
#         elif op == '/':
#             return num1 / num2
#         elif op == '*':
#             return num1 * num2
#         else:
#             print('Operações +, -, *, /')
#
# while True:
#     num1 = input('Digite um numero: ')
#     num2 = input('Digite um numero: ')
#     if not num1.isnumeric() or not num2.isnumeric():
#         print('Você precisa digitar um numero.')
#         continue
#
#     op = input('Digite um operador: ')
#
#     print('Resultado:', calculadora(num1, op, num2))

def soma():
    num1 = float(input('Digite um Numero: '))
    num2 = float(input('Digite um Numero: '))
    soma = num1 + num2
    print(f'{num1} + {num2} = {soma}')


def subt():
    num1 = float(input('Digite um Numero: '))
    num2 = float(input('Digite um Numero: '))
    subt = num1 - num2
    print(f'{num1} - {num2} = {subt}')


def multi():
    num1 = float(input('Digite um Numero: '))
    num2 = float(input('Digite um Numero: '))
    multi = num1 * num2
    print(f'{num1} * {num2} = {multi}')


def divi():
    num1 = float(input('Digite um Numero: '))
    num2 = float(input('Digite um Numero: '))
    divi = num1 / num2
    print(f'{num1} / {num2} = {divi}')


def continuar():
    continuar = input('Deseja Continuar? S/N ')
    if continuar in ['S', 's']:
        main()
    else:
        continuar = 'N'


def sair():
    exit()


def main():
    print('\n Operadores \n'
          '\n 1 - Soma '
          '\n 2 - Subtração '
          '\n 3 - Multiplicação '
          '\n 4 - Divisão '
          '\n 0 - Sair \n')
    try:
        operador = int(input('Qual Operação Deseja? '))

        if operador == 1:
            soma()
            continuar()
        elif operador == 2:
            subt()
            continuar()
        elif operador == 3:
            multi()
            continuar()
        elif operador == 4:
            divi()
            continuar()
    except:
        print('Valor inválido')
        continuar()
        if continuar == 'N':
            exit()

main()