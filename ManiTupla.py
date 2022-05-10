# Criando Tuplas

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f'O quinto elemento da Tupla é: {tupla[4]}')

print(f'O quinto elemento da Tupla é: {tupla[-1]}')

tupla_slicing = tupla[4:]
print(tupla_slicing)

# del tupla

print(f'A quantidade de elementos iguais à 1: {tupla.count(1)}')
print(f'O elemento 10 está na posição: {tupla.index(10)}')


for elemento in tupla:
    print(f'Elemento: {elemento}')