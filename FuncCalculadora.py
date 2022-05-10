def soma(numeros):
    return int(numeros[0]) + int(numeros[1])


def divisao(numeros):
    return int(numeros[0]) / int(numeros[1])


def subtracao(numeros):
    return int(numeros[0]) - int(numeros[1])


def multiplicacao(numeros):
    return int(numeros[0]) * int(numeros[1])


numeros_input = input('Digite os números separados por espaço: ').split(' ')
operacao_input = input('Digite a operação (+ / - *): ')
resultado_calculo = 0

if len(numeros_input) != 2:
    print('Quantidade de entradas difernete de 2')
else:
    if operacao_input in '+/-*':
        if operacao_input == '+':
            resultado_calculo = soma(numeros_input)

        elif operacao_input == '/':
            resultado_calculo = divisao(numeros_input)

        elif operacao_input == '-':
            resultado_calculo = subtracao(numeros_input)

        elif operacao_input == '*':
            resultado_calculo = multiplicacao(numeros_input)

        print(f'Resultado: {resultado_calculo}')

    else:
        print(f'Operação {operacao_input} inválida!')