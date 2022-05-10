sacola = ['Arroz', 'Feijão', 'Carne', 'Farinha']

print(f'A Lista Inicial é: {sacola}')

# Adiciona um Item ao fim da lista

sacola.append('Macarrão')
print(f'A Lista depois da Chamada do Append() é: {sacola}')

# Adiciona Todos os itens de outra estrutura ao fim da lista

sacola.extend(['Maionese', 'Ketchup'])
print(f'A Lista depois da Chamada do Extend() é: {sacola}')

# Insere um item na posição desejada

sacola.insert(0, 'Milho')
print(f'A Lista depois da Chamada do Insert() é: {sacola}')

# Remove o primeiro elemento igual ao valor passado

sacola.remove('Macarrão')
print(f'A Lista depois da Chamada do Remove() é: {sacola}')

# Remove o item da posição desejada da lista e o retorna
# Caso o indice não seja especificado, retorna o ultimo elemento

sacola.pop(3)
print(f'A Lista depois da Chamada do POP() é: {sacola}')

# Remove todos os elementos da lista

# sacola.clear()
# print(f'A Lista depois da Chamada do Clear() é: {sacola}')

# Retorna o indice do primeiro elemento do valor especificado

print(sacola.index('Milho'))

# Conta o numero de ocorrencias do valor especificado na lista

print(sacola.count('Arroz'))

# Ordena os itens da lista

sacola.sort()
print(f'A Lista depois da Chamada do Sort() é: {sacola}')

# Reverte os elementos da lista

sacola.reverse()
print(f'A Lista depois da Chamada do Reverse() é: {sacola}')

# Retorna uma lista com a cópia dos elementos da lista de origem

copia_sacola = sacola.copy()
print(f'A Lista depois da Chamada do Copy() é: {copia_sacola}')