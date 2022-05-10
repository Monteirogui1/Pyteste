while True:
    print()

    num1 = input('Digite um numero: ')
    num2 = input('Digite um numero: ')
    op = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um numero.')
        continue
    num1 = int(num1)
    num2 = int(num2)

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '*':
        print(num1 * num2)
    else:
        print('Operações +, -, *, /')
