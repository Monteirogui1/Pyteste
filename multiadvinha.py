lista = list(range(0, 48, 8))
print(lista)
num = str(lista[5])
chances = 3

while True:
    ad = input('0, 8, 16, 24, 32, x? ')

    if ad in num:
        print(f'Numero {ad} Existe.')
    else:
        print(f'Numero {ad} não existe !')

    if ad == num:
        print('Você ganhou!')
        break

    if chances <= 0:
        print('Você perdeu')

    if ad not in num:
        chances -= 1
    print(f'Você tem mais {chances} chances.')