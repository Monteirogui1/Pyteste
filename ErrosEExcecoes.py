"""
try:
    # Código a ser testado

except:
    # Execute esse código caso um erro ocorra

else:
    # Execute esse código caso nenhum erro ocorra

finally:
    # Sempre execute esse código

"""


def divide_dois_numeros(dividendo, divisor):
    return dividendo / divisor


try:
    # Código a ser testado
    numero_1 = int(input('Digite um numero: '))
    numero_2 = int(input('Digite outro numero: '))

    resultado = divide_dois_numeros(numero_1, numero_2)

except (ZeroDivisionError, TypeError) as e:
    print(f'Divisão por zero não suportada ou Erro de Tipagem! Erro: {e}')

except:
    # Execute esse código caso um erro ocorra
    print('Um erro aconteceu!')

else:
    # Execute esse código caso nenhum erro ocorra
    print(resultado)

finally:
    # Sempre execute esse código
    print('Finalizando o programa...')