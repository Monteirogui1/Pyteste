from random import randint

cap_max_balde = 1000

balde = 0

while balde <= cap_max_balde:
    volume_copo = randint(95, 100)

    print(f'O copo foi enchido com {volume_copo}mls')

    balde += volume_copo

    print(f'O Volume do Balde é de {balde}mls\n')

print(f'O Volume do Balde ultrapassou a capacidade máxima de {cap_max_balde}mls e está com {balde}mls')
