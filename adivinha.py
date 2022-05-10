secreto = 'secreto'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) < 1:
        print('Só vale uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()

    secreto_temp = ''
    for letra_sec in secreto:
        if letra_sec in digitadas:
            secreto_temp += letra_sec
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Você ganhou, a palavra era {secreto_temp}')
        break
    else:
        print(f'A palavra está assim: {secreto_temp}')

    if letra not in secreto:
        chances -= 1
    print(f'Você só tem {chances} Chances!')
    print()