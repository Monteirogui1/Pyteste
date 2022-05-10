computador = {
    'cpu': 'Ryzen5 5600G',
    'ram': 'DDR4 16GB',
    'gpu': 'GTX 1660 8GB',
    'ssd': 'Samsung 256GB',

}

print(f'Compuatador V1 {computador}')

computador['fonte'] = 'Fonte 600W'

print(f'Compuatdor V2 {computador}')

computador.update({'fonte': 'Fonte 850w', 'ssd': 'Samsung 1TB'})

print(f'Compuatdor V3 {computador}')