def monta_computador(cpu, memoria, hd, *precos, monitor=17, **kwargs):
    print('O computador montado foi:')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memoria}GB')
    print(f'\tHD: {hd}TB')
    print(f'\tMonitor: {monitor} Polegadas')
    print('\tOutros Atributos:')

    for chave, valor in kwargs.items():
        print(f'\t\t {chave}: {valor}')

    print(f'\tPreços praticados: ')
    for preco in precos:
        print(f'\t\t R$ {preco:.2f}')


monta_computador('I7', 16, 5, 2500, 3600, 5500, monitor=25, Webcam='Webcam Multilaser', Teclado='Corsair')
