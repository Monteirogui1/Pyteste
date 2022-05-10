#cpf = '16395834754'
while True:
    cpf = input('Digite um cpf: ')
    novocpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total = int(novocpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11

        d = 11 - (total % 11)

        if d > 9:
            d = 0
            total = 0
            novocpf += str(d)

    sequencia = novocpf == str(novocpf[0]) * len(cpf)

    if cpf == novocpf:
        print('Valido')
    else:
        print('Invalido')