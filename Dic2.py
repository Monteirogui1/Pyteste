fila = {
    '0': 'João',
    '1': 'Joana',
    '2': 'Ana',
    '3': 'Clara',
    '4': 'Silva'
}

print(f'Fila inicial: {fila}')

#del
del fila['0']
print(f'Fila Atualizada: {fila}')

#pop
valor_retirado = fila.pop('1')
print(f'Valor retirado: {valor_retirado}')
print(f'Fila Atualizada: {fila}')

#popitem
fila.popitem()
print(f'Fila Atualizada: {fila}')

#clear
fila.clear()
print(f'Fila Atualizada: {fila}')
