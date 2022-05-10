cadastro = {
    'id': 1,
    'nome': 'João Carlos',
    'filhos': ['Lara', 'Ste' ],
    'compras': [
        {
            'id': 785,
            'produto': 'Vaso',
            'preco': 599.99
        }
    ]
}

produtos_compra = cadastro['compras'][0]


print(f'O Cliente {cadastro["nome"]} comprou {produtos_compra["produto"]} por {produtos_compra["preco"]}  ')