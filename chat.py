def saudacao(msg='Ola', name='Usuario'):
    print(msg, name)


saudacao('Olá', 'Gui')

print()

def soma(n1, n2, n3):
    return n1 + n2 - n3


som = soma(3, 5, 1)
print(som)

print()

def percentual(n1, por):
    return n1 + (n1 * por / 100)

per = percentual(1500, 20)
print(per)

