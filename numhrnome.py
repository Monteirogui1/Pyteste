num = input('Digite um numero: ')


if num.isdigit():
    num = int(num)
    print('Numero Inteiro')
    if num % 2 == 0:
        print(f'{num} Par')
    else:
        print(f'{num} Ímpar')

else:
    print('Não é Inteiro')


